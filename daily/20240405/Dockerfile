FROM ubuntu:20.04

# Set versions
ENV SPARK_VERSION=2.4.5
ENV HADOOP_VERSION=3.2.1
ENV SCALA_VERSION=2.11
ENV SCALA_BINARY_VERSION=2.11
ENV AWS_SDK_VERSION=1.11.375
ENV MAVEN_VERSION=3.8.4
ENV HIVE_VERSION=2.3.7

# Set environment variables
ENV SPARK_HOME=/opt/spark
ENV HADOOP_HOME=/opt/hadoop
ENV MAVEN_HOME=/opt/maven
ENV JAVA_HOME=/usr/lib/jvm/java-8-openjdk-amd64
ENV PATH=$MAVEN_HOME/bin:$JAVA_HOME/bin:$PATH:$SPARK_HOME/bin:$HADOOP_HOME/bin

# Install dependencies
RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get install -y \
    openjdk-8-jdk \
    git \
    curl \
    wget \
    python3 \
    python3-pip \
    software-properties-common \
    ssh \
    net-tools \
    ca-certificates \
    && update-alternatives --install /usr/bin/python python /usr/bin/python3 1 \
    && ln -s /usr/bin/pip3 /usr/bin/pip \
    && rm -rf /var/lib/apt/lists/*

# Install Maven
RUN mkdir -p ${MAVEN_HOME} && \
    curl -fsSL https://archive.apache.org/dist/maven/maven-3/${MAVEN_VERSION}/binaries/apache-maven-${MAVEN_VERSION}-bin.tar.gz | \
    tar -xz --strip-components=1 -C ${MAVEN_HOME}

# Create directory for the Spark source code
WORKDIR /opt/spark-src

# IMPORTANT: We'll use COPY instead of git clone to bring in the local modified source code
# Copy the local Spark source code (with custom modifications)
COPY . .

# Set up Hadoop version in pom.xml files
# We're assuming the main pom.xml has been modified to use Hadoop 3.2.1
# But we'll add this step to ensure consistency across all module pom files
RUN find . -name pom.xml -exec sed -i "s/<hadoop.version>2.6.[0-9]<\/hadoop.version>/<hadoop.version>${HADOOP_VERSION}<\/hadoop.version>/g" {} \; && \
    find . -name pom.xml -exec sed -i "s/<hadoop.binary.version>2.6.[0-9]<\/hadoop.binary.version>/<hadoop.binary.version>${HADOOP_VERSION}<\/hadoop.binary.version>/g" {} \;

# Build Spark with Hadoop 3.2.1 and Hive support
RUN ./dev/make-distribution.sh \
    --name hadoop3-s3a-hive \
    --pip \
    --tgz \
    -Phadoop-${HADOOP_VERSION} \
    -Pyarn \
    -Phive \
    -Phive-thriftserver \
    -Dhadoop.version=${HADOOP_VERSION} \
    -Dhive.version=${HIVE_VERSION} \
    -DskipTests

# Unpack the built Spark distribution
RUN mkdir -p ${SPARK_HOME} && \
    tar -xzf /opt/spark-src/spark-${SPARK_VERSION}-bin-hadoop3-s3a-hive.tgz -C /opt && \
    mv /opt/spark-${SPARK_VERSION}-bin-hadoop3-s3a-hive/* ${SPARK_HOME} && \
    rm -rf /opt/spark-${SPARK_VERSION}-bin-hadoop3-s3a-hive.tgz

# Download Hadoop to get the necessary libraries
RUN wget -q https://archive.apache.org/dist/hadoop/common/hadoop-${HADOOP_VERSION}/hadoop-${HADOOP_VERSION}.tar.gz && \
    tar -xzf hadoop-${HADOOP_VERSION}.tar.gz && \
    mv hadoop-${HADOOP_VERSION} ${HADOOP_HOME} && \
    rm hadoop-${HADOOP_VERSION}.tar.gz

# Download additional dependencies for S3A committer and Hive
RUN wget -q https://repo1.maven.org/maven2/org/apache/hadoop/hadoop-aws/${HADOOP_VERSION}/hadoop-aws-${HADOOP_VERSION}.jar -P ${SPARK_HOME}/jars/ && \
    wget -q https://repo1.maven.org/maven2/com/amazonaws/aws-java-sdk-bundle/${AWS_SDK_VERSION}/aws-java-sdk-bundle-${AWS_SDK_VERSION}.jar -P ${SPARK_HOME}/jars/ && \
    wget -q https://repo1.maven.org/maven2/org/apache/hive/hive-exec/${HIVE_VERSION}/hive-exec-${HIVE_VERSION}.jar -P ${SPARK_HOME}/jars/ && \
    wget -q https://repo1.maven.org/maven2/org/apache/hive/hive-metastore/${HIVE_VERSION}/hive-metastore-${HIVE_VERSION}.jar -P ${SPARK_HOME}/jars/

# Create Hive warehouse directory and configure permissions
RUN mkdir -p /user/hive/warehouse && \
    chmod -R 777 /user/hive

# Copy configuration files
COPY spark-defaults.conf ${SPARK_HOME}/conf/spark-defaults.conf
COPY core-site.xml ${HADOOP_HOME}/etc/hadoop/core-site.xml
COPY hive-site.xml ${SPARK_HOME}/conf/hive-site.xml

# Clean up source code to reduce image size
RUN rm -rf /opt/spark-src

# Set up working directory
WORKDIR ${SPARK_HOME}

# Expose Spark ports
EXPOSE 4040 8080 7077 6066

# Set default command
CMD ["bin/spark-shell"]
