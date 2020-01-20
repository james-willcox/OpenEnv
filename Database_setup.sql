CREATE  TABLE openenv.measurement ( 
	measurement_id       serial  primary key ,
	direction            numeric(20,6)   ,
	measurement_type_id  integer   ,
	latitude             numeric(12,6)   ,
	longitude            numeric(12,6)   ,
	measurement_datetime timestamptz   ,
	station_id           integer   ,
	measurement_value    numeric(12,6)
 );

COMMENT ON TABLE openenv.measurement IS 'The primary table for this platform.  It will store all the raw data results for the OpenEnv system';

COMMENT ON COLUMN openenv.measurement.direction IS 'for a vector quantity, this is the bearing, i.e. wind direction';
;


CREATE  TABLE openenv.measurement_type ( 
	measurement_type_id  serial  NOT NULL ,
	measurement_type     varchar(255)   ,
	units                varchar(255)   ,
	description          text   ,
	effective_from       timestamptz   ,
	effective_to         timestamptz   ,
	CONSTRAINT pk_measurement_type_measurement_type_id PRIMARY KEY ( measurement_type_id )
 );

COMMENT ON COLUMN openenv.measurement_type.measurement_type IS 'The title of the measurement, i.e. temperature';

COMMENT ON COLUMN openenv.measurement_type.units IS 'What are the units that this measurement is measured in, i.e. degrees c';

COMMENT ON COLUMN openenv.measurement_type.effective_from IS 'UTC date the record was effective from';

COMMENT ON COLUMN openenv.measurement_type.effective_to IS 'UTC effective to date of the record, NULL if record is still effective';
;


CREATE  TABLE openenv.station ( 
	station_id           serial  NOT NULL ,
	account_id           integer   ,
	station_api_key      varchar(256)   ,
	station_type_id      integer   ,
	CONSTRAINT pk_station_station_id PRIMARY KEY ( station_id )
 );

COMMENT ON TABLE openenv.station IS 'This is the station that recorded the measurement';
;


CREATE  TABLE openenv.station_type ( 
	station_type_id      serial  NOT NULL ,
	type_label           varchar(126)   ,
	description          varchar(500)   ,
	CONSTRAINT pk_station_type_station_type_id PRIMARY KEY ( station_type_id )
 );

CREATE  TABLE openenv.account ( 
	account_id           serial  NOT NULL ,
	first_name           varchar(100)   ,
	last_name            varchar(100)   ,
	email                varchar(256)   ,
	sign_up_date         timestamptz   ,
	CONSTRAINT pk_account_account_id PRIMARY KEY ( account_id )
 );

COMMENT ON TABLE openenv.account IS 'A users account details';




CREATE  TABLE openenv.account_api_key ( 
	api_key_id           serial  NOT NULL ,
	account_id           integer   ,
	api_key              varchar(256)   ,
	CONSTRAINT pk_account_api_key_api_key_id PRIMARY KEY ( api_key_id )
 );


CREATE  TABLE openenv.login_details ( 
	login_details_id     serial  NOT NULL ,
	account_id           integer   ,
	account_password     varchar(256)   ,
	modified_date        timestamptz   ,
	CONSTRAINT pk_login_details_login_details_id PRIMARY KEY ( login_details_id )
 );



CREATE  TABLE openenv.station_location ( 
	station_location_id  serial  NOT NULL ,
	station_id           integer   ,
	latitude             numeric(12,6)   ,
	longitude            numeric(12,6)   ,
	effective_from_date  timestamptz   ,
	effective_to_date    timestamptz   ,
	CONSTRAINT pk_station_location_station_location_id PRIMARY KEY ( station_location_id )
 );

COMMENT ON TABLE openenv.station_location IS 'measurements of the stations location';



