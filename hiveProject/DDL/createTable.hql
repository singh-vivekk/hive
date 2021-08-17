CREATE TABLE myTable
(
  date string,
  state string,
  confirmed string,
  recovered string,
  deceased string,
  other string,
  tested string
  )
ROW FORMAT Delimited
FIELDS TERMINATED BY ',';