from pyspark.sql.types import StructType, StructField, StringType, IntegerType, DateType, LongType, DecimalType, DoubleType, BooleanType

# schema定义
def get_schemas():
    member_schema = StructType([
        StructField("memberuid", LongType(), nullable=False),
        StructField("birthyear", IntegerType(), nullable=True),
        StructField("gendercode", StringType(), nullable=True),
        StructField("statecode", StringType(), nullable=True),
        StructField("zip3value", StringType(), nullable=True),
        StructField("raceethnicitytypecode", StringType(), nullable=True),
        StructField("createddate", DateType(), nullable=False)
    ])

    memberenrollment_schema = StructType([
        StructField("memberuid", LongType(), nullable=False),
        StructField("effectivedate", DateType(), nullable=False),
        StructField("terminationdate", DateType(), nullable=False),
        StructField("payergroupcode", StringType(), nullable=True),
        StructField("payertypecode", StringType(), nullable=True),
        StructField("productcode", StringType(), nullable=True),
        StructField("medicalindicator", IntegerType(), nullable=False),
        StructField("rxindicator", IntegerType(), nullable=False),
        StructField("sourceid", IntegerType(), nullable=True),
        StructField("groupplantypecode", StringType(), nullable=True),
        StructField("macontracttypecode", StringType(), nullable=True),
        StructField("acaindicator", IntegerType(), nullable=True),
        StructField("acaissuerstatecode", StringType(), nullable=True),
        StructField("acagrandfatheredindicator", IntegerType(), nullable=True),
        StructField("acaonexchangeindicator", IntegerType(), nullable=True),
        StructField("acametallevel", StringType(), nullable=True),
        StructField("acaactuarialvalue", IntegerType(), nullable=True),
        StructField("createddate", DateType(), nullable=False)
    ])

    memberenrollment_adjusted_schema = StructType([
        StructField("memberuid", LongType(), nullable=True),
        StructField("effectivedate", DateType(), nullable=True),
        StructField("terminationdate", DateType(), nullable=True),
        StructField("claimadiustedeffectivedate", DateType(), nullable=True),
        StructField("claimadjustedterminationdate", DateType(), nullable=True),
        StructField("rxclaimadiustedeffectivedate", DateType(), nullable=True),
        StructField("rxclaimadiustedterminationdate", DateType(), nullable=True),
        StructField("payergroupcode", StringType(), nullable=True),
        StructField("payertypecode", StringType(), nullable=True),
        StructField("productcode", StringType(), nullable=True),
        StructField("medicalindicator", IntegerType(), nullable=True),
        StructField("rxindicator", IntegerType(), nullable=True),
        StructField("sourceid", IntegerType(), nullable=True),
        StructField("groupplantypecode", StringType(), nullable=True),
        StructField("macontracttypecode", StringType(), nullable=True),
        StructField("acaindicator", IntegerType(), nullable=True),
        StructField("acaissuerstatecode", StringType(), nullable=True),
        StructField("acagrandfatheredindicator", IntegerType(), nullable=True),
        StructField("acaonexchangeindicator", IntegerType(), nullable=True),
        StructField("acametallevel", StringType(), nullable=True),
        StructField("acaactuarialvalue", IntegerType(), nullable=True),
        StructField("createddate", DateType(), nullable=True)
    ])

    provider_schema = StructType([
        StructField("provideruid", IntegerType(), nullable=False),
        StructField("lastname", StringType(), nullable=True),
        StructField("firstname", StringType(), nullable=True),
        StructField("middlename", StringType(), nullable=True),
        StructField("companyname", StringType(), nullable=True),
        StructField("npi1", StringType(), nullable=True),
        StructField("npitypecode1", StringType(), nullable=True),
        StructField("parentorganization1", StringType(), nullable=True),
        StructField("npi2", StringType(), nullable=True),
        StructField("npitypecode2", StringType(), nullable=True),
        StructField("parentorganization2", StringType(), nullable=True),
        StructField("primarypracticeaddress", StringType(), nullable=True),
        StructField("secondarypracticeaddress", StringType(), nullable=True),
        StructField("practicecity", StringType(), nullable=True),
        StructField("practicestate", StringType(), nullable=True),
        StructField("practicezip", StringType(), nullable=True),
        StructField("practicezip4", StringType(), nullable=True),
        StructField("practicephone", StringType(), nullable=True),
        StructField("primarybillingaddress", StringType(), nullable=True),
        StructField("secondarybillingaddress", StringType(), nullable=True),
        StructField("billingcity", StringType(), nullable=True),
        StructField("billingstate", StringType(), nullable=True),
        StructField("billingzip", StringType(), nullable=True),
        StructField("billingzip4", StringType(), nullable=True),
        StructField("billingphone", StringType(), nullable=True),
        StructField("taxonomycode1", StringType(), nullable=True),
        StructField("taxonomytypel", StringType(), nullable=True),
        StructField("taxonomyclassification1", StringType(), nullable=True),
        StructField("taxonomyspecialization1", StringType(), nullable=True),
        StructField("taxonomycode2", StringType(), nullable=True),
        StructField("taxonomytype2", StringType(), nullable=True),
        StructField("taxonomyclassification2", StringType(), nullable=True),
        StructField("taxonomyspecialization2", StringType(), nullable=True),
        StructField("createddate", DateType(), nullable=False)
    ])

    providersupplemental_schema = StructType([
        StructField("provideruid", IntegerType(), nullable=False),
        StructField("nameprefix", StringType(), nullable=True),
        StructField("name", StringType(), nullable=True),
        StructField("namesuffix", StringType(), nullable=True),
        StructField("address1", StringType(), nullable=True),
        StructField("address2", StringType(), nullable=True),
        StructField("city", StringType(), nullable=True),
        StructField("state", StringType(), nullable=True),
        StructField("zip", StringType(), nullable=True),
        StructField("phone", StringType(), nullable=True),
        StructField("fax", StringType(), nullable=True),
        StructField("deanumber", StringType(), nullable=True),
        StructField("npinumber", StringType(), nullable=True),
        StructField("createddate", DateType(), nullable=False)
    ])

    claim_schema = StructType([
        StructField("claimuid", LongType(), nullable=False),
        StructField("memberuid", LongType(), nullable=False),
        StructField("provideruid", LongType(), nullable=True),
        StructField("claimstatuscode", StringType(), nullable=True),
        StructField("servicedate", DateType(), nullable=False),
        StructField("servicethrudate", DateType(), nullable=False),
        StructField("ubpatientdischargestatuscode", StringType(), nullable=True),
        StructField("serviceunitquantity", IntegerType(), nullable=True),
        StructField("denieddayscount", IntegerType(), nullable=True),
        StructField("billedamount", DecimalType(19, 4), nullable=True),
        StructField("allowedamount", DecimalType(19, 4), nullable=True),
        StructField("copayamount", DecimalType(19, 4), nullable=True),
        StructField("paidamount", DecimalType(19, 4), nullable=True),
        StructField("costamount", DecimalType(19, 4), nullable=True),
        StructField("rxproviderindicator", IntegerType(), nullable=False),
        StructField("pcpproviderindicator", IntegerType(), nullable=False),
        StructField("roomboardindicator", IntegerType(), nullable=False),
        StructField("majorsurgeryindicator", IntegerType(), nullable=False),
        StructField("excludefromdischargeindicator", IntegerType(), nullable=False),
        StructField("claimformtypecode", StringType(), nullable=True),
        StructField("institutionaltypecode", StringType(), nullable=True),
        StructField("professionaltypecode", StringType(), nullable=True),
        StructField("billingprovideruid", LongType(), nullable=True),
        StructField("renderingprovideruid", LongType(), nullable=True),
        StructField("renderingprovidernpi", StringType(), nullable=True),
        StructField("billingprovidernpi", StringType(), nullable=True),
        StructField("sourcemodifieddate", DateType(), nullable=True),
        StructField("claimnumber", StringType(), nullable=True),
        StructField("claimlinenumber", StringType(), nullable=True),
        StructField("createddate", DateType(), nullable=False)
    ])

    claimcode_schema = StructType([
        StructField("claimuid", LongType(), nullable=False),
        StructField("memberuid", LongType(), nullable=False),
        StructField("servicedate", DateType(), nullable=False),
        StructField("servicethrudate", DateType(), nullable=False),
        StructField("codetype", IntegerType(), nullable=False),
        StructField("ordinalposition", IntegerType(), nullable=False),
        StructField("codevalue", StringType(), nullable=False),
        StructField("derivedindicator", IntegerType(), nullable=False),
        StructField("createddate", DateType(), nullable=False)
    ])

    rxclaim_schema = StructType([
        StructField("rxclaimuid", LongType(), nullable=False),
        StructField("memberuid", LongType(), nullable=False),
        StructField("provideruid", LongType(), nullable=True),
        StructField("claimstatuscode", StringType(), nullable=True),
        StructField("filldate", DateType(), nullable=False),
        StructField("ndc11code", StringType(), nullable=True),
        StructField("supplydayscount", IntegerType(), nullable=True),
        StructField("dispensedquantity", DoubleType(), nullable=True),
        StructField("billedamount", DecimalType(19, 4), nullable=True),
        StructField("allowedamount", DecimalType(19, 4), nullable=True),
        StructField("copayamount", DecimalType(19, 4), nullable=True),
        StructField("paidamount", DecimalType(19, 4), nullable=True),
        StructField("costamount", DecimalType(19, 4), nullable=True),
        StructField("prescribingnpi", StringType(), nullable=True),
        StructField("dispensingnpi", StringType(), nullable=True),
        StructField("sourcemodifieddate", DateType(), nullable=True),
        StructField("createddate", DateType(), nullable=False)
    ])

    labclaim_schema = StructType([
        StructField("labclaimuid", LongType(), nullable=False),
        StructField("memberuid", LongType(), nullable=False),
        StructField("provideruid", LongType(), nullable=True),
        StructField("claimstatuscode", StringType(), nullable=True),
        StructField("servicedate", DateType(), nullable=True),
        StructField("cptcode", StringType(), nullable=True),
        StructField("loinccode", StringType(), nullable=True),
        StructField("resultnumber", DoubleType(), nullable=True),
        StructField("resulttext", StringType(), nullable=True),
        StructField("posnegresultindicator", BooleanType(), nullable=True),
        StructField("unitname", StringType(), nullable=True),
        StructField("sourcemodifieddate", DateType(), nullable=True),
        StructField("createddate", DateType(), nullable=False)
    ])

    dischargestatuscodes_schema = StructType([
        StructField("code", StringType(), nullable=False),
        StructField("description", StringType(), nullable=True)
    ])

    payertypecodes_schema = StructType([
        StructField("code", StringType(), nullable=False),
        StructField("description", StringType(), nullable=True)
    ])

    placeofservicecodes_schema = StructType([
        StructField("code", StringType(), nullable=False),
        StructField("name", StringType(), nullable=True),
        StructField("description", StringType(), nullable=True)
    ])

    claimcodetype_schema = StructType([
        StructField("codetype", IntegerType(), nullable=False),
        StructField("name", StringType(), nullable=True),
        StructField("description", StringType(), nullable=True)
    ])

    diabetescodes_schema = StructType([
        StructField("code", StringType(), nullable=False),
        StructField("description", StringType(), nullable=True),
        StructField("type", StringType(), nullable=True)
    ])

    upkmemberkeys_schema = StructType([
        StructField("upk_key_1", StringType(), nullable=True),
        StructField("upk_key_2", StringType(), nullable=True),
        StructField("upk_key_4", StringType(), nullable=True),
        StructField("upk_key_7", StringType(), nullable=True),
        StructField("birth_dt", StringType(), nullable=True),
        StructField("gender_cd", StringType(), nullable=True),
        StructField("zip3", StringType(), nullable=True),
        StructField("memberuid", IntegerType(), nullable=True)
    ])

    consolidated_claim_price_schema = StructType([
        StructField("claimheaderuid", LongType(), nullable=True),
        StructField("claimlinenumber", LongType(), nullable=True),
        StructField("claimstatuscode", StringType(), nullable=True),
        StructField("memberuid", LongType(), nullable=True),
        StructField("billingprovidernpi", StringType(), nullable=True),
        StructField("billingprovideruid", LongType(), nullable=True),
        StructField("renderingprovidernpi", StringType(), nullable=True),
        StructField("renderingprovideruid", LongType(), nullable=True),
        StructField("providertaxonomycode", StringType(), nullable=True),
        StructField("pcpproviderindicator", IntegerType(), nullable=True),
        StructField("rxproviderindicator", IntegerType(), nullable=True),
        StructField("servicedate", DateType(), nullable=True),
        StructField("servicethrudate", DateType(), nullable=True),
        StructField("admissiondate", DateType(), nullable=True),
        StructField("dischargedate", DateType(), nullable=True),
        StructField("claimformtypecode", StringType(), nullable=True),
        StructField("servicetype", StringType(), nullable=True),
        StructField("medicarefeeschedule", StringType(), nullable=True),
        StructField("tobcode", StringType(), nullable=True),
        StructField("msdrgcode", StringType(), nullable=True),
        StructField("ubpatientdischargestatuscode", StringType(), nullable=True),
        StructField("denieddayscount", LongType(), nullable=True),
        StructField("ubrevenuecode", StringType(), nullable=True),
        StructField("roomboardindicator", IntegerType(), nullable=True),
        StructField("poscode", StringType(), nullable=True),
        StructField("hcpcscode", StringType(), nullable=True),
        StructField("hcpcsmodifiercode1", StringType(), nullable=True),
        StructField("hcpcsmodifiercode2", StringType(), nullable=True),
        StructField("hcpcsmodifiercode3", StringType(), nullable=True),
        StructField("hcpcsmodifiercode4", StringType(), nullable=True),
        StructField("majorsurgeryindicator", IntegerType(), nullable=True),
        StructField("serviceunitquantity", LongType(), nullable=True),
        StructField("allowedamount", DecimalType(19, 4), nullable=True),
        StructField("copayamount", DecimalType(19, 4), nullable=True),
        StructField("paidamount", DecimalType(19, 4), nullable=True),
        StructField("pricingbundledflag", BooleanType(), nullable=True),
        StructField("pricingallowedamount", DecimalType(19, 4), nullable=True),
        # ICD诊断码和手术码（假设最多25个）
        *(StructField(f"icdcmdxcode{i:02}", StringType(), nullable=True) for i in range(1, 26)),
        *(StructField(f"icdcmpxcode{i:02}", StringType(), nullable=True) for i in range(1, 26)),
        StructField("createddate", DateType(), nullable=True)
    ])

    consolidated_claimxref_schema = StructType([
        StructField("claimuid", LongType(), nullable=False),
        StructField("claimheaderuid", LongType(), nullable=True),
        StructField("claimlinenumber", LongType(), nullable=True)
    ])

    consolidated_enrollment_monthly_schema = StructType([
        StructField("memberuid", LongType(), nullable=False),
        StructField("monthbegindate", DateType(), nullable=True),
        StructField("monthenddate", DateType(), nullable=True),
        StructField("payergroupcode", StringType(), nullable=True),
        StructField("payertypecode", StringType(), nullable=True),
        StructField("productcode", StringType(), nullable=True),
        StructField("medicalindicator", IntegerType(), nullable=True),
        StructField("rxindicator", IntegerType(), nullable=True),
        StructField("macontracttypecode", StringType(), nullable=True),
        StructField("groupplantypecode", StringType(), nullable=True),
        StructField("acaindicator", IntegerType(), nullable=True),
        StructField("acaissuerstatecode", StringType(), nullable=True),
        StructField("acagrandfatheredindicator", IntegerType(), nullable=True),
        StructField("acaonexchangeindicator", IntegerType(), nullable=True),
        StructField("acametallevel", StringType(), nullable=True),
        StructField("acaactuarialvalue", StringType(), nullable=True),
        StructField("sourceid", StringType(), nullable=True),
        StructField("createddate", DateType(), nullable=True)
    ])

    consolidated_rxclaim_price_schema = StructType([
        StructField("rxclaimfilluid", LongType(), nullable=True),
        StructField("claimstatuscode", StringType(), nullable=True),
        StructField("memberuid", LongType(), nullable=True),
        StructField("provideruid", LongType(), nullable=True),
        StructField("providernpi", StringType(), nullable=True),
        StructField("prescribingnpi", StringType(), nullable=True),
        StructField("dispensingnpi", StringType(), nullable=True),
        StructField("filldate", DateType(), nullable=True),
        StructField("ndc11code", StringType(), nullable=True),
        StructField("supplydayscount", LongType(), nullable=True),
        StructField("dispensedquantity", DoubleType(), nullable=True),
        StructField("allowedamount", DecimalType(19, 4), nullable=True),
        StructField("copayamount", DecimalType(19, 4), nullable=True),
        StructField("paidamount", DecimalType(19, 4), nullable=True),
        StructField("pricingallowedamount", DecimalType(19, 4), nullable=True),
        StructField("createddate", DateType(), nullable=True)
    ])

    consolidated_rxclaimxref_schema = StructType([
        StructField("rxclaimuid", LongType(), nullable=True),
        StructField("rxclaimfilluid", LongType(), nullable=True)
    ])

    APDRG_schema = StructType([
        StructField("DRG", IntegerType(), nullable=True),
        StructField("medsurg", StringType(), nullable=True),
        StructField("MDC", StringType(), nullable=True),
        StructField("longdescription", StringType(), nullable=True)  # 使用 StringType 假设描述不超过默认长度限制
    ])

    MSDRG_schema = StructType([
        StructField("code", IntegerType(), nullable=True),
        StructField("description", StringType(), nullable=True)
    ])

    providertypecodes_schema = StructType([
        StructField("code", StringType(), nullable=True),
        StructField("description", StringType(), nullable=True)
    ])

    zip3sociodemographiccollapse_schema = StructType([
        StructField("origzip3", IntegerType(), nullable=True),
        StructField("DominantZip3", IntegerType(), nullable=True),
        StructField("fullzip3collapsecode", StringType(), nullable=True),
        StructField("reportablestate", StringType(), nullable=True)
    ])

    ubrevenuecodes_schema = StructType([
        StructField("id", IntegerType(), nullable=True),
        StructField("UBRevenueCode", IntegerType(), nullable=True),
        StructField("description", StringType(), nullable=True)
    ])

    typeofbillcodes_schema = StructType([
        StructField("sno", IntegerType(), nullable=True),
        StructField("tobcode", StringType(), nullable=True),
        StructField("description", StringType(), nullable=True)
    ])

    consolidated_labclaim_schema = StructType([
        StructField("labclaimresultuid", LongType(), nullable=True),
        StructField("claimstatuscode", StringType(), nullable=True),
        StructField("memberuid", LongType(), nullable=True),
        StructField("provideruid", LongType(), nullable=True),
        StructField("providernpi", StringType(), nullable=True),
        StructField("servicedate", DateType(), nullable=True),
        StructField("hcpcscode", StringType(), nullable=True),
        StructField("loinccode", StringType(), nullable=True),
        StructField("posnegresultindicator", BooleanType(), nullable=True),
        StructField("unitname", StringType(), nullable=True),
        StructField("createddate", DateType(), nullable=True)
    ])

    consolidated_labclaimxref_schema = StructType([
        StructField("labclaim", LongType(), nullable=True),
        StructField("labclaimresultuid", LongType(), nullable=True)
    ])

    claim_price_schema = StructType([
        StructField("claimuid", LongType(), nullable=True),
        StructField("memberuid", LongType(), nullable=True),
        StructField("providerid", StringType(), nullable=True),
        StructField("servicedate", DateType(), nullable=True),
        StructField("servicethrudate", DateType(), nullable=True),
        StructField("hcpcscode", StringType(), nullable=True),
        StructField("hcpcsmodifiercode1", StringType(), nullable=True),
        StructField("hcpcsmodifiercode2", StringType(), nullable=True),
        StructField("ubrevenuecode", StringType(), nullable=True),
        StructField("serviceunitquantity", IntegerType(), nullable=True),
        StructField("admissiondate", DateType(), nullable=True),
        StructField("dischargedate", DateType(), nullable=True),
        StructField("ubpatientdischargestatuscode", StringType(), nullable=True),
        StructField("servicetype", StringType(), nullable=True),
        StructField("medicarefeeschedule", StringType(), nullable=True),
        StructField("encounterid", StringType(), nullable=True),
        StructField("pricing_hcpcscode", StringType(), nullable=True),
        StructField("pricing_apccode", StringType(), nullable=True),
        StructField("pricing_drgcode", StringType(), nullable=True),
        StructField("pricing_hippscode", StringType(), nullable=True),
        StructField("pricing_revcode", StringType(), nullable=True),
        StructField("pricing_los", DecimalType(19, 1), nullable=True),
        StructField("pricing_bundledflag", BooleanType(), nullable=True),
        StructField("pricing_allowedamount", DecimalType(25, 2), nullable=True),
        StructField("createddate", DateType(), nullable=True)
    ])

    rxclaim_price_schema = StructType([
        StructField("rxclaimuid", LongType(), nullable=True),
        StructField("memberuid", LongType(), nullable=True),
        StructField("providerid", StringType(), nullable=True),
        StructField("filldate", DateType(), nullable=True),
        StructField("ndc11code", StringType(), nullable=True),
        StructField("supplydayscount", IntegerType(), nullable=True),
        StructField("quantitydispensed", DecimalType(19, 3), nullable=True),
        StructField("pricing_allowedamount", DecimalType(18, 2), nullable=True),
        StructField("createddate", DateType(), nullable=True)
    ])

    consolidated_provider_schema = StructType([
        StructField("provideruid", IntegerType(), nullable=True),
        StructField("lastname", StringType(), nullable=True),
        StructField("firstname", StringType(), nullable=True),
        StructField("middlename", StringType(), nullable=True),
        StructField("companyname", StringType(), nullable=True),
        StructField("npi1", StringType(), nullable=True),
        StructField("npitypecode1", StringType(), nullable=True),
        StructField("parentorganization1", StringType(), nullable=True),
        StructField("npi2", StringType(), nullable=True),
        StructField("npitypecode2", StringType(), nullable=True),
        StructField("parentorganization2", StringType(), nullable=True),
        StructField("primarypracticeaddress", StringType(), nullable=True),
        StructField("secondarypracticeaddress", StringType(), nullable=True),
        StructField("practicecity", StringType(), nullable=True),
        StructField("practicestate", StringType(), nullable=True),
        StructField("practicezip", StringType(), nullable=True),
        StructField("practicezip4", StringType(), nullable=True),
        StructField("practicephone", StringType(), nullable=True),
        StructField("primarybillingaddress", StringType(), nullable=True),
        StructField("secondarybillingaddress", StringType(), nullable=True),
        StructField("billingcity", StringType(), nullable=True),
        StructField("billingstate", StringType(), nullable=True),
        StructField("billingzip", StringType(), nullable=True),
        StructField("billingzip4", StringType(), nullable=True),
        StructField("billingphone", StringType(), nullable=True),
        StructField("taxonomycode1", StringType(), nullable=True),
        StructField("taxonomytype1", StringType(), nullable=True),
        StructField("taxonomyclassification1", StringType(), nullable=True),
        StructField("taxonomyspecialization1", StringType(), nullable=True),
        StructField("taxonomycode2", StringType(), nullable=True),
        StructField("taxonomytype2", StringType(), nullable=True),
        StructField("taxonomyclassification2", StringType(), nullable=True),
        StructField("taxonomyspecialization2", StringType(), nullable=True),
        StructField("sourcenameprefix", StringType(), nullable=True),
        StructField("sourcename", StringType(), nullable=True),
        StructField("sourcenamesuffix", StringType(), nullable=True),
        StructField("sourceaddress1", StringType(), nullable=True),
        StructField("sourceaddress2", StringType(), nullable=True),
        StructField("sourcecity", StringType(), nullable=True),
        StructField("sourcestate", StringType(), nullable=True),
        StructField("sourcezip", StringType(), nullable=True),
        StructField("sourcephone", StringType(), nullable=True),
        StructField("sourcefax", StringType(), nullable=True),
        StructField("sourcedeanumber", StringType(), nullable=True),
        StructField("createddate", DateType(), nullable=True)
    ])

    return {
        "member": member_schema,
        "memberenrollment": memberenrollment_schema,
        "memberenrollment_adjusted": memberenrollment_adjusted_schema,
        "provider": provider_schema,
        "providersupplemental": providersupplemental_schema,
        "claim": claim_schema,
        "claimcode": claimcode_schema,
        "rxclaim": rxclaim_schema,
        "labclaim": labclaim_schema,
        "dischargestatuscodes": dischargestatuscodes_schema,
        "payertypecodes": payertypecodes_schema,
        "placeofservicecodes": placeofservicecodes_schema,
        "claimcodetype": claimcodetype_schema,
        "diabetescodes": diabetescodes_schema,
        "upkmemberkeys": upkmemberkeys_schema,
        "consolidated_claim_price": consolidated_claim_price_schema,
        "consolidated_claimxref": consolidated_claimxref_schema,
        "consolidated_enrollment_monthly": consolidated_enrollment_monthly_schema,
        "consolidated_rxclaim_price": consolidated_rxclaim_price_schema,
        "consolidated_rxclaimxref": consolidated_rxclaimxref_schema,
        "APDRG": APDRG_schema,
        "MSDRG": MSDRG_schema,
        "providertypecodes": providertypecodes_schema,
        "zip3sociodemographiccollapse": zip3sociodemographiccollapse_schema,
        "ubrevenuecodes": ubrevenuecodes_schema,
        "typeofbillcodes": typeofbillcodes_schema,
        "consolidated_labclaim": consolidated_labclaim_schema,
        "consolidated_labclaimxref": consolidated_labclaimxref_schema,
        "claim_price": claim_price_schema,
        "rxclaim_price": rxclaim_price_schema,
        "consolidated_provider": consolidated_provider_schema
    }
