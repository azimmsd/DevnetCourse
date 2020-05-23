import json
jsonstr="""{
  "people": [
    {
      "Id": "1",
      "FirstName": "Ehsan",
      "LastName": "Masoudi"
    },
    {
      "Id": "2",
      "FirstName": "Mehrnoosh",
      "LastName": "Entezami"
    },
    {
      "Id": "3",
      "FirstName": "Iman",
      "LastName": "Rajabizadeh"
    }
  ]
}"""
jsonobj=json.loads(jsonstr)
print(jsonobj)  