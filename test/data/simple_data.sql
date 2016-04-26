# ...

# PROGRESS MARK

INSERT INTO [commodities] ([name]) VALUES ('Pencils');
INSERT INTO [commodities] ([name]) VALUES ('Pens');
INSERT INTO [nodes] ([name]) VALUES ('Seattle');
INSERT INTO [nodes] ([name]) VALUES ('Boston');
INSERT INTO [nodes] ([name]) VALUES ('New York');
INSERT INTO [nodes] ([name]) VALUES ('Denver');
INSERT INTO [nodes] ([name]) VALUES ('Detroit');
INSERT INTO [cost] ([commodity],[source],[destination],[cost]) VALUES ('Pencils','Denver','Seattle',30.0);
INSERT INTO [cost] ([commodity],[source],[destination],[cost]) VALUES ('Pens','Denver','Seattle',30.0);
INSERT INTO [cost] ([commodity],[source],[destination],[cost]) VALUES ('Pencils','Detroit','New York',20.0);
INSERT INTO [cost] ([commodity],[source],[destination],[cost]) VALUES ('Pens','Detroit','New York',20.0);
INSERT INTO [cost] ([commodity],[source],[destination],[cost]) VALUES ('Pens','Detroit','Boston',20.0);
INSERT INTO [cost] ([commodity],[source],[destination],[cost]) VALUES ('Pencils','Detroit','Boston',10.0);
INSERT INTO [cost] ([commodity],[source],[destination],[cost]) VALUES ('Pens','Detroit','Seattle',80.0);
INSERT INTO [cost] ([commodity],[source],[destination],[cost]) VALUES ('Pens','Denver','New York',70.0);
INSERT INTO [cost] ([commodity],[source],[destination],[cost]) VALUES ('Pens','Denver','Boston',60.0);
INSERT INTO [cost] ([commodity],[source],[destination],[cost]) VALUES ('Pencils','Denver','New York',40.0);
INSERT INTO [cost] ([commodity],[source],[destination],[cost]) VALUES ('Pencils','Detroit','Seattle',60.0);
INSERT INTO [cost] ([commodity],[source],[destination],[cost]) VALUES ('Pencils','Denver','Boston',40.0);
INSERT INTO [arcs] ([source],[destination],[capacity]) VALUES ('Detroit','Seattle',120.0);
INSERT INTO [arcs] ([source],[destination],[capacity]) VALUES ('Denver','Seattle',120.0);
INSERT INTO [arcs] ([source],[destination],[capacity]) VALUES ('Detroit','New York',80.0);
INSERT INTO [arcs] ([source],[destination],[capacity]) VALUES ('Denver','New York',120.0);
INSERT INTO [arcs] ([source],[destination],[capacity]) VALUES ('Denver','Boston',120.0);
INSERT INTO [arcs] ([source],[destination],[capacity]) VALUES ('Detroit','Boston',100.0);
INSERT INTO [inflow] ([commodity],[node],[quantity]) VALUES ('Pens','Boston',-40.0);
INSERT INTO [inflow] ([commodity],[node],[quantity]) VALUES ('Pens','New York',-30.0);
INSERT INTO [inflow] ([commodity],[node],[quantity]) VALUES ('Pencils','Detroit',50.0);
INSERT INTO [inflow] ([commodity],[node],[quantity]) VALUES ('Pencils','Seattle',-10.0);
INSERT INTO [inflow] ([commodity],[node],[quantity]) VALUES ('Pencils','Denver',60.0);
INSERT INTO [inflow] ([commodity],[node],[quantity]) VALUES ('Pens','Detroit',60.0);
INSERT INTO [inflow] ([commodity],[node],[quantity]) VALUES ('Pens','Seattle',-30.0);
INSERT INTO [inflow] ([commodity],[node],[quantity]) VALUES ('Pens','Denver',40.0);
INSERT INTO [inflow] ([commodity],[node],[quantity]) VALUES ('Pencils','New York',-50.0);
INSERT INTO [inflow] ([commodity],[node],[quantity]) VALUES ('Pencils','Boston',-50.0);
