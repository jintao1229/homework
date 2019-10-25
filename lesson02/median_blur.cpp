#include<iostream>
#include<opencv2/imgproc/imgproc.hpp>
#include <opencv2/opencv.hpp>
using namespace std;
using namespace cv;

//对三个数进行排序
void sort_in_three(vector<uchar> &arr) {
	if (arr[0] > arr[1]) {
		uchar min = arr[1];
		arr[1] = arr[0];
		arr[0] = min;
	}

	if (arr[1] <= arr[2]) {
		return;
	}
	else if(arr[2] <= arr[1] && arr[2] > arr[0])
	{
		uchar min = arr[2];
		arr[2] = arr[1];
		arr[1] = min;
	}
	else {
		uchar min = arr[2];
		arr[2] = arr[1];
		arr[1] = arr[0];
		arr[0] = min;
	}

	return;
}

//对2个数组归并排序
vector<uchar> merge_sort_two(vector<uchar> arr1 , vector<uchar> arr2) {
	vector<uchar> res;
	int p1 = 0, p2 = 0;

	for (int i = 0; i < arr1.size()+ arr2.size(); i++) {
		if (p1 == arr1.size()) {
			res.push_back(arr2[p2++]);
			continue;
		}
		if (p2 == arr2.size()) {
			res.push_back(arr1[p1++]);
			continue;
		}
		if (arr1[p1] < arr2[p2]) {
			res.push_back(arr1[p1++]);
		}
		else {
			res.push_back(arr2[p2++]);
		}
	}
	return res;
}

int median_blur(Mat &src,Mat &dst) {
	int rows = src.rows;
	int cols = src.cols;
	vector<uchar> left_arr = { 0,0,0 };
	vector<uchar> mid_arr = { 0,0,0 };
	vector<uchar> right_arr = { 0,0,0 };
	   
	for (int r = 1; r < rows-1; ++r) {
		uchar* pData1 = src.ptr<uchar>(r-1);
		uchar* pData2 = src.ptr<uchar>(r);
		uchar* pData3 = src.ptr<uchar>(r+1);

		uchar* pData_dst = dst.ptr<uchar>(r);

		left_arr[0] = pData1[0];
		left_arr[1] = pData2[0];
		left_arr[2] = pData3[0];

		sort_in_three(left_arr);
		mid_arr[0] = pData1[1];
		mid_arr[1] = pData2[1];
		mid_arr[2] = pData3[1];
		sort_in_three(mid_arr);

		for (int c = 1; c < cols - 1; ++c) {
			right_arr[0] = pData1[c + 1];
			right_arr[1] = pData2[c + 1];
			right_arr[2] = pData3[c + 1];
			sort_in_three(right_arr);
			vector<uchar> r = merge_sort_two(merge_sort_two(left_arr, mid_arr), right_arr);
			pData_dst[c] = r[4];
			left_arr = mid_arr;
			mid_arr = right_arr;

		}
	}
	return 0;
}
int main()
{
	Mat src = imread("C:/Users/45479/Desktop/ps.png", 0);
	Mat dst_median(src.size(), src.type());
	median_blur(src, dst_median);
	imshow("src", src);
	imshow("1", dst_median);
	waitKey();
	//system("pause");
	return 0;
}
