# Dew-Mesh Simulator

This simulator application is derived from the Meshtastic interactive simulator in the comments below. All the original work was written by GUVWAF (github.com/GUVWAF). The additions to this application can be found within the ./interactive.py and interactiveSim.py files. The additional code produces:
1. More transparent node communication in the main running terminal. This includes details of each transferred packet, radio type used, sender/recipient details and text data.
2. The transmission radio type used in each packet. They are arbitrary types for reference purposes only. No code was changed to an individual radio's RSSI, SNR, transmission distance or other characteristics. The is because the simulator is the LoRa radio itself and cannot be altered without significant changes to the mesh interface or Linux native application.
3. The final graphed pathway results, updated with radio type for each packet.

Please note the "program" file is not usable and must be created with the use of Visual Studio Code and PlatformIO.


## Meshtasticator
interactive simulator for [Meshtastic](https://meshtastic.org/). 

## Interactive simulator
The interactive simulator uses the [Linux native application of Meshtastic](https://meshtastic.org/docs/software/linux-native), i.e. the real device software, while simulating some of the hardware interfaces, including the LoRa chip. 

See [this document](INTERACTIVE_SIM.md) for a usage guide. 

It allows for debugging multiple communicating nodes without having real devices. 

https://user-images.githubusercontent.com/78759985/193409669-e8b6be37-6c73-40b3-84a4-8757ab4b7dfd.mp4

Furthermore, since the simulator has an 'oracle view' of the network, it allows to visualize the route messages take. 

![](/img/route_plot.png)

## License
Part of the source code is based on [this repo](https://github.com/lucagioacchini/lora-network-simulator), which eventually stems from [1].

This work is licensed under a [Creative Commons Attribution 4.0 International License](https://creativecommons.org/licenses/by/4.0/). 

## References
1. [S. Spinsante, L. Gioacchini and L. Scalise, "A novel experimental-based tool for the design of LoRa networks," 2019 II Workshop on Metrology for Industry 4.0 and IoT (MetroInd4.0&IoT), 2019, pp. 317-322, doi: 10.1109/METROI4.2019.8792833.](https://ieeexplore.ieee.org/document/8792833)
2. [Martin C. Bor, Utz Roedig, Thiemo Voigt, and Juan M. Alonso, "Do LoRa Low-Power Wide-Area Networks Scale?", In Proceedings of the 19th ACM International Conference on Modeling, Analysis and Simulation of Wireless and Mobile Systems (MSWiM '16), 2016. Association for Computing Machinery, New York, NY, USA, 59–67.](https://doi.org/10.1145/2988287.2989163)

