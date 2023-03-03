

CREATE TABLE "Biospecimen" (
	"hasStudy" TEXT, 
	"hasParticipant" TEXT, 
	"sampleId" TEXT NOT NULL, 
	"sampleType" TEXT NOT NULL, 
	"ageAtBiospecimenCollection" INTEGER, 
	"parentSampleId" TEXT, 
	"parentSampleType" TEXT, 
	"collectionId" TEXT, 
	"collectionSampleType" TEXT, 
	"containerId" TEXT, 
	volume FLOAT, 
	"volumeUnit" TEXT, 
	"laboratoryProcedure" TEXT, 
	"biospecimenStorage" TEXT, 
	"sampleAvailability" VARCHAR(11), 
	PRIMARY KEY ("hasStudy", "hasParticipant", "sampleId", "sampleType", "ageAtBiospecimenCollection", "parentSampleId", "parentSampleType", "collectionId", "collectionSampleType", "containerId", volume, "volumeUnit", "laboratoryProcedure", "biospecimenStorage", "sampleAvailability")
);

CREATE TABLE "Condition" (
	"hasStudy" TEXT, 
	"hasParticipant" TEXT, 
	"eventId" TEXT, 
	"eventType" TEXT, 
	"conditionSourceText" TEXT, 
	"ageAtConditionObservation" INTEGER, 
	"conditionInterpretation" VARCHAR(12), 
	"conditionStatus" VARCHAR(10), 
	"conditionDataSource" VARCHAR(13), 
	"hpoLabel" TEXT, 
	"hpoCode" TEXT, 
	"mondoLabel" TEXT, 
	"mondoCode" TEXT, 
	"maxoLabel" TEXT, 
	"maxoCode" TEXT, 
	"otherLabel" TEXT, 
	"otherCode" TEXT, 
	"measureType" TEXT, 
	"measureValue" INTEGER, 
	"measureUnit" TEXT, 
	"ageAtMeasurement" INTEGER, 
	PRIMARY KEY ("hasStudy", "hasParticipant", "eventId", "eventType", "conditionSourceText", "ageAtConditionObservation", "conditionInterpretation", "conditionStatus", "conditionDataSource", "hpoLabel", "hpoCode", "mondoLabel", "mondoCode", "maxoLabel", "maxoCode", "otherLabel", "otherCode", "measureType", "measureValue", "measureUnit", "ageAtMeasurement")
);

CREATE TABLE "DataFile" (
	"hasStudy" TEXT, 
	"hasParticipant" TEXT, 
	"hasBiospecimen" TEXT, 
	"fileId" TEXT, 
	"fileName" TEXT NOT NULL, 
	"fileHash" TEXT, 
	"dataAccess" VARCHAR(10), 
	"dataCategory" TEXT NOT NULL, 
	"dataType" TEXT, 
	"experimentalStrategy" TEXT, 
	"experimentalPlatform" TEXT, 
	"fileFormat" TEXT NOT NULL, 
	"fileSize" INTEGER, 
	"fileSizeUnit" TEXT, 
	"accessUrl" TEXT, 
	"publicationDoi" TEXT, 
	PRIMARY KEY ("hasStudy", "hasParticipant", "hasBiospecimen", "fileId", "fileName", "fileHash", "dataAccess", "dataCategory", "dataType", "experimentalStrategy", "experimentalPlatform", "fileFormat", "fileSize", "fileSizeUnit", "accessUrl", "publicationDoi")
);

CREATE TABLE "Participant" (
	"hasStudy" TEXT, 
	"participantId" TEXT, 
	"participantExternalId" TEXT NOT NULL, 
	"familyId" TEXT, 
	"familyType" VARCHAR(12) NOT NULL, 
	"fatherId" TEXT, 
	"motherId" TEXT, 
	"siblingId" TEXT, 
	"otherFamilyMemberId" TEXT, 
	"familyRelationship" VARCHAR(17), 
	sex VARCHAR(7) NOT NULL, 
	race VARCHAR(41) NOT NULL, 
	ethnicity VARCHAR(22) NOT NULL, 
	"downSyndromeStatus" VARCHAR(3) NOT NULL, 
	"ageAtFirstPatientEngagement" INTEGER NOT NULL, 
	"firstPatientEngagementEvent" TEXT NOT NULL, 
	"outcomesVitalStatus" VARCHAR(24), 
	"ageAtLastVitalStatus" INTEGER, 
	PRIMARY KEY ("hasStudy", "participantId", "participantExternalId", "familyId", "familyType", "fatherId", "motherId", "siblingId", "otherFamilyMemberId", "familyRelationship", sex, race, ethnicity, "downSyndromeStatus", "ageAtFirstPatientEngagement", "firstPatientEngagementEvent", "outcomesVitalStatus", "ageAtLastVitalStatus")
);

CREATE TABLE "Study" (
	"studyCode" VARCHAR(13) NOT NULL, 
	"studyName" TEXT NOT NULL, 
	program VARCHAR(7) NOT NULL, 
	dbgap TEXT, 
	PRIMARY KEY ("studyCode", "studyName", program, dbgap)
);
