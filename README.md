# Energy-Disaggregation

Link to the video- https://drive.google.com/drive/folders/1dVdfrLnnsNcIj4Cr3faYGytYpVBT91AX?usp=sharing 
Energy disaggregation refers to the process in which we are able to tell the energy consumption of each appliance in home given the reading of mains

For the code mentioned above, first 170 lines are preparing data for the network. The data used in this case is REDD dataset. For different appliances,different model will be trained. 
In the above code, I trained the model only for dishwasher. There are 2 input for the model created- Auxillary input and differential input.

Auxillary input is just the mains reading. For the REDD dataset, there were two mains reading for each houe, so the auxillary input shape taken is (None,499,499)
,where 499 is the legth of the sequence for each mains reading. If we start at time t, then the sequence mentioned will end at time t+499 for each mains

Differential input is the difference between consecutive mains reading i.e reading at time t+1-reading at time t. After calculating the difference, the same input shape
array is created(None,499,499) where each window is sequence of difference in mains reading.

We taken differential input because deaggregation  can be taken as a denoising process. If we differentiate the raw aggregate power then the noise of an appliance is distinguishable.

For the model mentioned after line 170, two inputs in form of a list is given to the model. First element of the list is auxillary input and the second element is differential input

Now for the target variable, target variable is taken according to the seq2point approach instead of outputting corroesponding window output for corroesponding
input window at time t.

If window length is W, and first element is at time t, ten the appliance reading for which the model is to trained is taken for time t+W/2. That is the
middle element.

The above code is unique on its approach and has taken inspiration from below mentioned papers:-

https://www.sciencedirect.com/science/article/pii/S2212827119307243

https://www.aaai.org/ocs/index.php/AAAI/AAAI18/paper/viewPaper/16623
