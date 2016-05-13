# TEST DATA - NO LEAVE, COMMITMENT, FIELDOUT

INSERT INTO [days] ([dayseq]) VALUES (1);
INSERT INTO [days] ([dayseq]) VALUES (2);
INSERT INTO [days] ([dayseq]) VALUES (3);
INSERT INTO [days] ([dayseq]) VALUES (4);
INSERT INTO [days] ([dayseq]) VALUES (5);
INSERT INTO [days] ([dayseq]) VALUES (6);
INSERT INTO [days] ([dayseq]) VALUES (7);

INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (1,'Daily Van','DV1',7,1,'VAN 0700');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (2,'Daily Van','DV2',15,2,'VAN 1500');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (3,'Daily Van','DV3',23,2,'VAN 2300');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (4,'Daily Reception','DR1',7,0,'REC 0700');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (5,'Daily Reception','DR2',15,0,'REC 1500');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (6,'Daily Reception','DR3',23,0,'REC 2300');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (7,'Daily Sergeant','DS1',7,0,'SGT 0700');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (8,'Daily Sergeant','DS2',15,0,'SGT 1500');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (9,'Daily Sergeant','DS3',23,0,'SGT 2300');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (10,'Station General','SG1',8,0,'STAT 0800');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (11,'Station General','SG2',10,0,'STAT 1000');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (12,'Station General','SG3',13,0,'STAT 1300');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (13,'Station General','SG4',15,0,'STAT 1500');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (14,'Station Files','SF',8,1,'FILES 0800');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (15,'Other SafeStreets','OS',22,0,'SFST 2200');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (16,'Other Recovery','OR',17,0,'RECO 1700');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (17,'Leave','XX',6,0,'LEAVE');
INSERT INTO [shifts] ([shiftid],[type],[shift],[starttime],[crew],[description]) VALUES (18,'Not Rostered','XX',6,0,'REST');

INSERT INTO [members] ([memid],[ranknum],[lastname],[firstname]) VALUES (1,1,'','');
INSERT INTO [members] ([memid],[ranknum],[lastname],[firstname]) VALUES (2,1,'','');
INSERT INTO [members] ([memid],[ranknum],[lastname],[firstname]) VALUES (3,1,'','');
INSERT INTO [members] ([memid],[ranknum],[lastname],[firstname]) VALUES (4,2,'','');
INSERT INTO [members] ([memid],[ranknum],[lastname],[firstname]) VALUES (5,2,'','');
INSERT INTO [members] ([memid],[ranknum],[lastname],[firstname]) VALUES (6,2,'','');
INSERT INTO [members] ([memid],[ranknum],[lastname],[firstname]) VALUES (7,3,'','');
INSERT INTO [members] ([memid],[ranknum],[lastname],[firstname]) VALUES (8,3,'','');
INSERT INTO [members] ([memid],[ranknum],[lastname],[firstname]) VALUES (9,4,'','');
INSERT INTO [members] ([memid],[ranknum],[lastname],[firstname]) VALUES (10,4,'','');
INSERT INTO [members] ([memid],[ranknum],[lastname],[firstname]) VALUES (11,5,'','');
INSERT INTO [members] ([memid],[ranknum],[lastname],[firstname]) VALUES (12,6,'','');

INSERT INTO [carryover] ([memid],[lastweoff],[day0shift]) VALUES (1,-1,1);
INSERT INTO [carryover] ([memid],[lastweoff],[day0shift]) VALUES (2,-2,2);
INSERT INTO [carryover] ([memid],[lastweoff],[day0shift]) VALUES (3,-3,3);
INSERT INTO [carryover] ([memid],[lastweoff],[day0shift]) VALUES (4,-4,1);
INSERT INTO [carryover] ([memid],[lastweoff],[day0shift]) VALUES (5,-1,2);
INSERT INTO [carryover] ([memid],[lastweoff],[day0shift]) VALUES (6,-2,3);
INSERT INTO [carryover] ([memid],[lastweoff],[day0shift]) VALUES (7,-3,14);
INSERT INTO [carryover] ([memid],[lastweoff],[day0shift]) VALUES (8,-4,14);
INSERT INTO [carryover] ([memid],[lastweoff],[day0shift]) VALUES (9,-1,17);
INSERT INTO [carryover] ([memid],[lastweoff],[day0shift]) VALUES (10,-2,18);
INSERT INTO [carryover] ([memid],[lastweoff],[day0shift]) VALUES (11,-3,17);
INSERT INTO [carryover] ([memid],[lastweoff],[day0shift]) VALUES (12,-4,18);

INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (1,1,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (2,1,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (3,1,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (4,1,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (5,1,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (6,1,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (7,1,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (8,1,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (9,1,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (10,1,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (11,1,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (12,1,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (1,2,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (2,2,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (3,2,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (4,2,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (5,2,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (6,2,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (7,2,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (8,2,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (9,2,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (10,2,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (11,2,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (12,2,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (1,3,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (2,3,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (3,3,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (4,3,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (5,3,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (6,3,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (7,3,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (8,3,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (9,3,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (10,3,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (11,3,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (12,3,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (1,4,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (2,4,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (3,4,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (4,4,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (5,4,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (6,4,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (7,4,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (8,4,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (9,4,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (10,4,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (11,4,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (12,4,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (1,5,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (2,5,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (3,5,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (4,5,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (5,5,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (6,5,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (7,5,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (8,5,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (9,5,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (10,5,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (11,5,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (12,5,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (1,6,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (2,6,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (3,6,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (4,6,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (5,6,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (6,6,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (7,6,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (8,6,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (9,6,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (10,6,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (11,6,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (12,6,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (1,7,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (2,7,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (3,7,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (4,7,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (5,7,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (6,7,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (7,7,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (8,7,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (9,7,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (10,7,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (11,7,0);
INSERT INTO [leave] ([memid],[dayseq],[value]) VALUES (12,7,0);

INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (1,1,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (2,1,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (3,1,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (4,1,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (5,1,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (6,1,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (7,1,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (8,1,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (9,1,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (10,1,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (11,1,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (12,1,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (1,2,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (2,2,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (3,2,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (4,2,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (5,2,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (6,2,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (7,2,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (8,2,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (9,2,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (10,2,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (11,2,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (12,2,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (1,3,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (2,3,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (3,3,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (4,3,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (5,3,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (6,3,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (7,3,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (8,3,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (9,3,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (10,3,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (11,3,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (12,3,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (1,4,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (2,4,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (3,4,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (4,4,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (5,4,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (6,4,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (7,4,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (8,4,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (9,4,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (10,4,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (11,4,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (12,4,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (1,5,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (2,5,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (3,5,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (4,5,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (5,5,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (6,5,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (7,5,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (8,5,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (9,5,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (10,5,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (11,5,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (12,5,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (1,6,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (2,6,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (3,6,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (4,6,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (5,6,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (6,6,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (7,6,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (8,6,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (9,6,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (10,6,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (11,6,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (12,6,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (1,7,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (2,7,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (3,7,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (4,7,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (5,7,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (6,7,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (7,7,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (8,7,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (9,7,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (10,7,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (11,7,0);
INSERT INTO [commitment] ([memid],[dayseq],[value]) VALUES (12,7,0);

INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (1,1,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (2,1,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (3,1,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (4,1,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (5,1,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (6,1,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (7,1,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (8,1,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (9,1,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (10,1,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (11,1,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (12,1,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (1,2,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (2,2,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (3,2,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (4,2,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (5,2,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (6,2,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (7,2,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (8,2,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (9,2,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (10,2,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (11,2,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (12,2,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (1,3,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (2,3,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (3,3,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (4,3,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (5,3,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (6,3,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (7,3,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (8,3,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (9,3,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (10,3,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (11,3,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (12,3,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (1,4,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (2,4,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (3,4,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (4,4,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (5,4,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (6,4,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (7,4,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (8,4,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (9,4,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (10,4,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (11,4,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (12,4,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (1,5,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (2,5,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (3,5,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (4,5,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (5,5,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (6,5,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (7,5,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (8,5,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (9,5,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (10,5,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (11,5,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (12,5,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (1,6,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (2,6,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (3,6,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (4,6,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (5,6,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (6,6,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (7,6,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (8,6,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (9,6,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (10,6,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (11,6,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (12,6,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (1,7,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (2,7,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (3,7,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (4,7,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (5,7,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (6,7,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (7,7,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (8,7,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (9,7,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (10,7,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (11,7,0);
INSERT INTO [fieldout] ([memid],[dayseq],[value]) VALUES (12,7,0);
