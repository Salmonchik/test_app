CREATE TABLE figures (
	id UUID NOT NULL,
	created_at TIMESTAMP WITH TIME ZONE DEFAULT now(),
	dimension FLOAT NOT NULL,
	type VARCHAR NOT NULL,
	color VARCHAR NOT NULL,
	lat FLOAT NOT NULL,
	lon FLOAT NOT NULL,
	PRIMARY KEY (id)
)