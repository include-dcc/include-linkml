

CREATE TABLE "Assay" (
	"UsesBiospecimen" TEXT, 
	"HasOutput" TEXT, 
	PRIMARY KEY ("UsesBiospecimen", "HasOutput")
);

CREATE TABLE "Biospecimen" (
	"AgeAtBiospecimenCollection" INTEGER, 
	"BiospecimenStorage" TEXT, 
	"CollectionID" TEXT, 
	"CollectionSampleType" TEXT, 
	"ContainerID" TEXT, 
	"HasDatafile" TEXT, 
	"HasParticipant" TEXT, 
	"HasStudy" TEXT, 
	"LaboratoryProcedure" TEXT, 
	"ParentSampleID" TEXT, 
	"ParentSampleType" TEXT, 
	"SampleAvailability" VARCHAR(11), 
	"SampleID" TEXT NOT NULL, 
	"SampleType" TEXT NOT NULL, 
	"Volume" FLOAT, 
	"VolumeUnit" TEXT, 
	"HasAliquot" TEXT, 
	PRIMARY KEY ("AgeAtBiospecimenCollection", "BiospecimenStorage", "CollectionID", "CollectionSampleType", "ContainerID", "HasDatafile", "HasParticipant", "HasStudy", "LaboratoryProcedure", "ParentSampleID", "ParentSampleType", "SampleAvailability", "SampleID", "SampleType", "Volume", "VolumeUnit", "HasAliquot")
);

CREATE TABLE "Condition" (
	"HasParticipant" TEXT, 
	"AgeAtConditionObservation" INTEGER, 
	"MONDOLabel" TEXT, 
	"MONDOCode" TEXT, 
	"ConditionInterpretation" VARCHAR(12), 
	"ConditionDataSource" VARCHAR(13), 
	"HPOLabel" TEXT, 
	"HPOCode" TEXT, 
	"MAXOLabel" TEXT, 
	"MAXOCode" TEXT, 
	"OtherLabel" TEXT, 
	"OtherCode" TEXT, 
	PRIMARY KEY ("HasParticipant", "AgeAtConditionObservation", "MONDOLabel", "MONDOCode", "ConditionInterpretation", "ConditionDataSource", "HPOLabel", "HPOCode", "MAXOLabel", "MAXOCode", "OtherLabel", "OtherCode")
);

CREATE TABLE "DataFile" (
	"AccessURL" TEXT, 
	"CollectionID" TEXT, 
	"DataAccess" VARCHAR(10), 
	"DataCategory" TEXT NOT NULL, 
	"DataType" TEXT, 
	"ExperimentalStrategy" TEXT, 
	"FileID" TEXT, 
	"FileName" TEXT NOT NULL, 
	"Format" TEXT NOT NULL, 
	"HasBiospecimen" TEXT, 
	"HasParticipant" TEXT, 
	"HasStudy" TEXT, 
	"ParticipantID" TEXT NOT NULL, 
	"Size" TEXT, 
	"OriginalFileName" TEXT NOT NULL, 
	PRIMARY KEY ("AccessURL", "CollectionID", "DataAccess", "DataCategory", "DataType", "ExperimentalStrategy", "FileID", "FileName", "Format", "HasBiospecimen", "HasParticipant", "HasStudy", "ParticipantID", "Size", "OriginalFileName")
);

CREATE TABLE "FamilyGroup" (
	"HasParticipant" TEXT, 
	PRIMARY KEY ("HasParticipant")
);

CREATE TABLE "Participant" (
	"AgeAtLastVitalStatus" INTEGER, 
	"DownSyndromeStatus" VARCHAR(3) NOT NULL, 
	"Ethnicity" VARCHAR(22) NOT NULL, 
	"ExternalID" TEXT NOT NULL, 
	"FamilyID" TEXT, 
	"FamilyRelationship" TEXT, 
	"FamilyType" VARCHAR(12) NOT NULL, 
	"FatherID" TEXT, 
	"HasDatafile" TEXT, 
	"HasStudy" TEXT, 
	"MotherID" TEXT, 
	"OutcomesVitalStatus" VARCHAR(5), 
	"ParticipantID" TEXT NOT NULL, 
	"Race" VARCHAR(41) NOT NULL, 
	"Sex" VARCHAR(7) NOT NULL, 
	PRIMARY KEY ("AgeAtLastVitalStatus", "DownSyndromeStatus", "Ethnicity", "ExternalID", "FamilyID", "FamilyRelationship", "FamilyType", "FatherID", "HasDatafile", "HasStudy", "MotherID", "OutcomesVitalStatus", "ParticipantID", "Race", "Sex")
);

CREATE TABLE "Study" (
	"dbGap" TEXT, 
	"Program" VARCHAR(7) NOT NULL, 
	"StudyCode" VARCHAR(11) NOT NULL, 
	"StudyName" TEXT NOT NULL, 
	"HasParticipant" TEXT, 
	PRIMARY KEY ("dbGap", "Program", "StudyCode", "StudyName", "HasParticipant")
);
