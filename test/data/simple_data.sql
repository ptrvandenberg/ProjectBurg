# TEST DATA

INSERT INTO [days] ([dayseq]) VALUES (1);
INSERT INTO [days] ([dayseq]) VALUES (2);
INSERT INTO [days] ([dayseq]) VALUES (3);
INSERT INTO [days] ([dayseq]) VALUES (4);
INSERT INTO [days] ([dayseq]) VALUES (5);
INSERT INTO [days] ([dayseq]) VALUES (6);
INSERT INTO [days] ([dayseq]) VALUES (7);

INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (1,'Daily Van','DV1',7,2,'VAN 0700');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (2,'Daily Van','DV2',15,2,'VAN 1500');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (3,'Daily Van','DV3',23,2,'VAN 2300');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (4,'Daily Reception','DR1',7,2,'REC 0700');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (5,'Daily Reception','DR2',15,2,'REC 1500');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (6,'Daily Reception','DR3',23,2,'REC 2300');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (7,'Daily Sergeant','DS1',7,1,'SGT 0700');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (8,'Daily Sergeant','DS2',15,1,'SGT 1500');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (9,'Daily Sergeant','DS3',23,1,'SGT 2300');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (10,'Station General','SG1',8,0,'STAT 0800');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (11,'Station General','SG2',10,0,'STAT 1000');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (12,'Station General','SG3',13,0,'STAT 1300');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (13,'Station General','SG4',15,0,'STAT 1500');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (14,'Station Files','SF',8,2,'FILES 0800');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (15,'Other SafeStreets','OS',22,4,'SFST 2200');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (16,'Other Recovery','OR',17,0,'RECO 1700');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (98,'Leave','XX',6,0,'LEAVE');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (99,'Not Rostered','XX',6,0,'REST');

INSERT INTO [members] ([memid],[ranknum],[lastname],[firstname]) VALUES (,,'','');

INSERT INTO [carryover] ([memid],[lastweoff],[day0shift]) VALUES (,,);

INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (,,);

INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (,,);

INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (,,);
