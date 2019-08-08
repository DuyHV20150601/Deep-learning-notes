(1) pre-process a document input image and segment it into its blocks of content
    + convert into gray image
    +  running length algorithm
(2)use their vertical and horizontal projections to train
a CNN model for multi-class classification considering text,
image and table classes 
use VGG 
(3) detect new documents layout
using a pipeline including the trained CNN model