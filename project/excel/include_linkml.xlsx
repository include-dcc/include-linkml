

CREATE TABLE "Biospecimen" (
	age_at_biospecimen_collection TEXT, 
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
	sample_id TEXT, 
	sample_type TEXT, 
	volume TEXT, 
	volume_unit TEXT, 
	PRIMARY KEY (age_at_biospecimen_collection, biospecimen_storage, collection_id, collection_sample_type, container_id, has_datafile, has_participant, has_study, laboratory_procedure, parent_sample_id, parent_sample_type, sample_availability, sample_id, sample_type, volume, volume_unit)
);

CREATE TABLE "DataFile" (
	access_url TEXT, 
	collection_id TEXT, 
	data_access VARCHAR(10), 
	data_category TEXT, 
	data_type TEXT, 
	experimental_strategy TEXT, 
	file_id TEXT, 
	file_name TEXT, 
	format TEXT, 
	has_biospecimen TEXT, 
	has_participant TEXT, 
	has_study TEXT, 
	participant_id TEXT, 
	size TEXT, 
	PRIMARY KEY (access_url, collection_id, data_access, data_category, data_type, experimental_strategy, file_id, file_name, format, has_biospecimen, has_participant, has_study, participant_id, size)
);

CREATE TABLE "Participant" (
	age_at_diagnosis TEXT, 
	age_at_phenotype_assignment TEXT, 
	age_at_the_last_vital_status TEXT, 
	diagnosis_icd TEXT, 
	diagnosis_mondo TEXT, 
	diagnosis_ncit TEXT, 
	diagnosis_source_text TEXT, 
	diagnosis_type TEXT, 
	down_syndrome_status VARCHAR(3), 
	ethnicity VARCHAR(22), 
	external_id TEXT, 
	family_id TEXT, 
	family_relationship TEXT, 
	family_type VARCHAR(12), 
	father_id TEXT, 
	has_datafile TEXT, 
	has_study TEXT, 
	mother_id TEXT, 
	outcomes_vital_status TEXT, 
	participant_id TEXT, 
	phenotype_hpo TEXT, 
	phenotype_source_text TEXT, 
	phenotype_interpretation VARCHAR(12), 
	race VARCHAR(41), 
	sex VARCHAR(7), 
	PRIMARY KEY (age_at_diagnosis, age_at_phenotype_assignment, age_at_the_last_vital_status, diagnosis_icd, diagnosis_mondo, diagnosis_ncit, diagnosis_source_text, diagnosis_type, down_syndrome_status, ethnicity, external_id, family_id, family_relationship, family_type, father_id, has_datafile, has_study, mother_id, outcomes_vital_status, participant_id, phenotype_hpo, phenotype_source_text, phenotype_interpretation, race, sex)
);

CREATE TABLE "Study" (
	dbgap TEXT, 
	program VARCHAR(7), 
	study_code VARCHAR(10), 
	study_name TEXT, 
	PRIMARY KEY (dbgap, program, study_code, study_name)
);
