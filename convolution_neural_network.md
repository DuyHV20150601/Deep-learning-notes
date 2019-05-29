<h3>Convolution operation</h3> </p>
Convolution operation (tích chập) là một phương pháp được áp dụng trong nhiều bài toán thực tế . Trong Deep Learning, Convolution Operation được áp dụng trong mô hình Convolution Neural Network ,mô hình được ứng dụng rộng rãi trong computer vision hoặc natural language processing .</p>
Hình dưới đây minh họa cho convolution operator trong lĩnh vực computer vision:</p> 
<img src="img/img_convolution2.png"> </p>
Convolution operator bao gồm có 3 thành phần chính :</p>
* Input Image  </P> 
* Featrue Detector </p>
* Feature Map </p>
<h3>Input Image </h3> </p>
Là một multidimensional array (mảng đa chiều), đại diện cho đầu vào là một image.Image thường là những không gian màu như RGB , Grayscale , YUV ....</p>
Input Image là một mảng 2 chiều chứa 2 số là 0 và 1 .</p>
<h3>Feature detector</h3>
Hay còn được gọi là kernel hay filter cũng là một multidimensional array . Kernel giống như một cửa sổ trượt (sliding windows) dùng để quét hết tất cả các đặc trưng pixel trên ma trân input image bằng cách khi trượt tới ma trận con trên input image có cùng chiều thì thực hiện phép toán nhân ma trận vì thế những giá trị trên feature map là kết quả nhân ma trận của ma trân con cùng chiều của input image và kernel.</p>
Để hiểu thêm về phương pháp trượt của kernel có thể xem ở hinh minh họa dưới đây :</p>
<p>
<img src ='img/no_padding_no_strides.gif'>
</p>
<em> Nguồn: github.com/vdumoulin/conv_arithmetic</em> </p>
Input image là ma trận 4x4 màu xanh và kernel hay feature detector là ma trận 3x3 xanh đậm </p>
Sau khi trượt , kernel và ma trận con của input image sẽ thực hiện phép nhan 2 ma trận cùng chiều </p>
<p>
<img src = 'img/img_convole.png' alt ='hình ming họa'/> <em>Nguồn : Deep learning MIT </em>
</p>

