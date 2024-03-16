#!/bin/bash 

 

aws s3 mb s3://ds2002-mnk3kd 

curl https://www.alimentarium.org/sites/default/files/media/image/2017-02/AL027-01_pomme_de_terre_0_0.jpg > potato.png 

aws s3 cp potato.png s3://ds2002-mnk3kd/ 

aws s3 presign --expires-in 604800 s3://ds2002-mnk3kd/potato.png
https://ds2002-mnk3kd.s3.us-east-1.amazonaws.com/potato.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIA5FTZEJ2LHEPQYM3U%2F20240316%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240316T022812Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=FwoGZXIvYXdzEKP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaDFPjl7e11JmZT0ILKyLEAZMJAO2FqQzTHdSllxxdPxhRJOGlsPfl2bASJ9Fr0qP5yiA0ov6vna%2FUBnXwBPXAE9sSLJKcS%2Bf4tj3Qodv43l%2FoDefc8zS9t9N0GXJUXqW4In1Rwtycrn7HzaILvhImuApDpqt3MIMhtquys%2BLzF8TBaU5Unuj6QnLD9VL4zNioyaAykjGZBX6g6D%2FPJeXdndL4BXQLvb10I7fZExkLHUgdkuGFj5D2aAUZcuKr5uc2NT85gHqwBOOTYDKOeVkR6TY1xhUox%2B7TrwYyLSlFe1TTax4jwXxluyn0S5lNQnBcuSK9w5xU1ooj1UWoVIXdY5A6zBq3XNwk8A%3D%3D&X-Amz-Signature=2d4d30ec032bb804fee021e2dbea410d6e40a7031eb63d345884b1bb1374dcdf
