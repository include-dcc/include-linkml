

CREATE TABLE "Biospecimen" (
	age_at_biospecimen_collection__days INTEGER, 
	biospecimen_storage TEXT, 
	collection_id TEXT, 
	collection_sample_type TEXT, 
	container_id TEXT, 
	has_datafile TEXT, 
	has_participant TEXT, 
	has_study TEXT, 
	laboratory_procedure TEXT, 
	parent_sample_id TEXT, 
	parent_sample_type TEXT, 
	sample_availability VARCHAR(11), 
	sample_id TEXT NOT NULL, 
	sample_type TEXT, 
	volume TEXT, 
	volume_unit TEXT, 
	PRIMARY KEY (sample_id), 
	FOREIGN KEY(has_datafile) REFERENCES "DataFile" (file_id), 
	FOREIGN KEY(has_participant) REFERENCES "Participant" (participant_id)
);

CREATE TABLE "DataFile" (
	access_url TEXT, 
	collection_id TEXT, 
	data_access VARCHAR(10), 
	data_category TEXT, 
	data_type TEXT, 
	experimental_strategy TEXT, 
	file_id TEXT NOT NULL, 
	file_name TEXT, 
	format TEXT, 
	has_biospecimen TEXT, 
	has_participant TEXT, 
	has_study TEXT, 
	participant_id TEXT, 
	size TEXT, 
	PRIMARY KEY (file_id), 
	FOREIGN KEY(has_biospecimen) REFERENCES "Biospecimen" (sample_id), 
	FOREIGN KEY(has_participant) REFERENCES "Participant" (participant_id)
);

CREATE TABLE "Participant" (
	age_at_diagnosis__days INTEGER, 
	age_at_phenotype_assignment__days INTEGER, 
	age_at_the_last_vital_status__days INTEGER, 
	diagnosis__icd TEXT, 
	diagnosis__mondo TEXT, 
	diagnosis__ncit TEXT, 
	diagnosis__source_text TEXT, 
	diagnosis_type TEXT, 
	down_syndrome_status VARCHAR(3) NOT NULL, 
	ethnicity VARCHAR(22) NOT NULL, 
	external_id TEXT NOT NULL, 
	family_id TEXT, 
	family_relationship TEXT, 
	family_type VARCHAR(12), 
	father_id TEXT, 
	has_datafile TEXT, 
	has_study TEXT, 
	mother_id TEXT, 
	outcomes_vital_status TEXT, 
	participant_id TEXT NOT NULL, 
	phenotype__hpo TEXT, 
	phenotype__source_text TEXT, 
	phenotype_interpretation VARCHAR(12), 
	race VARCHAR(41) NOT NULL, 
	sex VARCHAR(7) NOT NULL, 
	PRIMARY KEY (participant_id), 
	FOREIGN KEY(has_datafile) REFERENCES "DataFile" (file_id)
);

CREATE TABLE "Study" (
	dbgap TEXT, 
	program VARCHAR(7) NOT NULL, 
	study_code VARCHAR(10) NOT NULL, 
	study_name TEXT NOT NULL, 
	PRIMARY KEY (dbgap, program, study_code, study_name)
);
