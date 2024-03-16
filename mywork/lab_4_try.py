#!/usr/bin/python3


import requests
url = 'https://media4.giphy.com/media/5GoVLqeAOo6PK/200w.gif?cid=6c09b9523bs95r6fmgy424cmkn9w434iyjdfqmn4iwfqu0b3&ep=v1_gifs_search&rid=200w.gif&ct=g'
r = requests.get(url, allow_redirects=True)

open('happy.
gif&ct=g
', 'wb').write(r.content)


bucket = 'ds2002-mnk3kd'
local_file = 'happy.
gif&ct=g
'

resp = s3.put_object(
    Body = local_file,
    Bucket = bucket,
    Key = local_file

ACL = 'public-read',

bucket_name = str
object_name = str
expires_in = int

response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in 604800
    )

)

