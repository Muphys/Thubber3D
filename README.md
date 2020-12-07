# Thubber3D

### To run the project

#### 1. Open [watch v61.f3d](https://github.com/Muphys/Thubber3D/blob/main/watch%20v61.f3d) with Fusion 360 and save it at least once.

<br/>

#### 2. Add [ThermalStudy.py](https://github.com/Muphys/Thubber3D/blob/main/ThermalStudy.py) into the Fusion 360 add-on list and run it. 

Your Fusion 360 may fail to respond for about 1 min but that's normal. You will see the thermal study result like this when finishing:

![image-20201206222757197](C:\Users\Muphy\AppData\Roaming\Typora\typora-user-images\image-20201206222757197.png)

<br/>

#### 3. Run this command in Fusion 360:

```
SimResults.ExportActiveResults D:\workplace\TestResult
```

This is for saving the study result as a VTU file. You may need to change the path according to your running environment. I was trying to integrate this step in the first script but it keep failing in Fusion 360. Running it myself works fine, however.

<br/>

#### 4. Run [ReadResult.py](https://github.com/Muphys/Thubber3D/blob/main/ReadResult.py) to access study results.

This script provides a plain method to access data in the VTU file exported in the last step, along with a visualization using matplotlib. To learn more about VTU format, please refer to [this](https://www.notion.so/VTU-Notes-11-5-2020-8f8d4a2621c3414598fc0d65ed245da4).

You can see a preliminary implementation of implanted trace if everything goes well so far.

![image-20201206222819487](C:\Users\Muphy\AppData\Roaming\Typora\typora-user-images\image-20201206222819487.png)

<br/>

Following-up supports for STL generation will be updated soon.