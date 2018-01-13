
// MatMFCDlg.cpp : 实现文件
//

#include "stdafx.h"
#include "MatMFC.h"
#include "MatMFCDlg.h"
#include "afxdialogex.h"

#ifdef _DEBUG
#define new DEBUG_NEW
#endif


// CMatMFCDlg 对话框

// 要显示的图   控件的ID
void CMatMFCDlg::DrawMat(cv::Mat& img, UINT nID)
{
	cv::Mat imgTmp;
	CRect rect;
	GetDlgItem(nID)->GetClientRect(&rect);  // 获取控件大小
	if (img.size() != cv::Size(rect.Width(), rect.Height()))
	{
		cv::resize(img, imgTmp, cv::Size(rect.Width(), rect.Height()));// 缩放Mat并备份
	}
	// 转一下格式 ,这段可以放外面,
	switch (imgTmp.channels())
	{
	case 1:
		cvtColor(imgTmp, imgTmp, CV_GRAY2BGRA); // GRAY单通道
		break;
	case 3:
		cvtColor(imgTmp, imgTmp, CV_BGR2BGRA);  // BGR三通道
		break;
	default:
		break;
	}
	int pixelBytes = imgTmp.channels()*(imgTmp.depth() + 1); // 计算一个像素多少个字节
	// 制作bitmapinfo(数据头)
	BITMAPINFO bitInfo;
	bitInfo.bmiHeader.biBitCount = 8 * pixelBytes;
	bitInfo.bmiHeader.biWidth = imgTmp.cols;
	bitInfo.bmiHeader.biHeight = -imgTmp.rows;
	bitInfo.bmiHeader.biPlanes = 1;
	bitInfo.bmiHeader.biSize = sizeof(BITMAPINFOHEADER);
	bitInfo.bmiHeader.biCompression = BI_RGB;
	bitInfo.bmiHeader.biClrImportant = 0;
	bitInfo.bmiHeader.biClrUsed = 0;
	bitInfo.bmiHeader.biSizeImage = 0;
	bitInfo.bmiHeader.biXPelsPerMeter = 0;
	bitInfo.bmiHeader.biYPelsPerMeter = 0;
	// Mat.data + bitmap数据头 -> MFC
	CDC *pDC = GetDlgItem(nID)->GetDC();
	::StretchDIBits(
		pDC->GetSafeHdc(),
		0, 0, rect.Width(), rect.Height(),
		0, 0, rect.Width(), rect.Height(),
		imgTmp.data,
		&bitInfo,
		DIB_RGB_COLORS,
		SRCCOPY
		);

	ReleaseDC(pDC);
}

CMatMFCDlg::CMatMFCDlg(CWnd* pParent /*=NULL*/)
	: CDialogEx(CMatMFCDlg::IDD, pParent)
{
	m_hIcon = AfxGetApp()->LoadIcon(IDR_MAINFRAME);
}

void CMatMFCDlg::DoDataExchange(CDataExchange* pDX)
{
	CDialogEx::DoDataExchange(pDX);
}

BEGIN_MESSAGE_MAP(CMatMFCDlg, CDialogEx)
	ON_WM_PAINT()
	ON_WM_QUERYDRAGICON()
	ON_BN_CLICKED(IDC_LOAD, &CMatMFCDlg::OnBnClickedLoad)
	ON_BN_CLICKED(IDC_EXIT, &CMatMFCDlg::OnBnClickedExit)
	ON_BN_CLICKED(IDC_SAVE, &CMatMFCDlg::OnBnClickedSave)
END_MESSAGE_MAP()


// CMatMFCDlg 消息处理程序

BOOL CMatMFCDlg::OnInitDialog()
{
	CDialogEx::OnInitDialog();

	// 设置此对话框的图标。  当应用程序主窗口不是对话框时，框架将自动
	//  执行此操作
	SetIcon(m_hIcon, TRUE);			// 设置大图标
	SetIcon(m_hIcon, FALSE);		// 设置小图标

	// TODO:  在此添加额外的初始化代码

	//// 显示控件大小，在表情符那里加一个断点就行
	//CRect rect;
	//GetDlgItem(IDC_IN1)->GetWindowRect(&rect);
	//int w = rect.Width(), h = rect.Height();
	//w = w;

	return TRUE;  // 除非将焦点设置到控件，否则返回 TRUE
}

// 如果向对话框添加最小化按钮，则需要下面的代码
//  来绘制该图标。  对于使用文档/视图模型的 MFC 应用程序，
//  这将由框架自动完成。

void CMatMFCDlg::OnPaint()
{
	// 读入背景图片
	src = cv::imread("src/II-VI MARLOW.jpg");
	DrawMat(src, IDC_IN2);

	if (IsIconic())
	{
		CPaintDC dc(this); // 用于绘制的设备上下文

		SendMessage(WM_ICONERASEBKGND, reinterpret_cast<WPARAM>(dc.GetSafeHdc()), 0);

		// 使图标在工作区矩形中居中
		int cxIcon = GetSystemMetrics(SM_CXICON);
		int cyIcon = GetSystemMetrics(SM_CYICON);
		CRect rect;
		GetClientRect(&rect);
		int x = (rect.Width() - cxIcon + 1) / 2;
		int y = (rect.Height() - cyIcon + 1) / 2;

		// 绘制图标
		dc.DrawIcon(x, y, m_hIcon);
	}
	else
	{
		CDialogEx::OnPaint();
	}
}

//当用户拖动最小化窗口时系统调用此函数取得光标
//显示。
HCURSOR CMatMFCDlg::OnQueryDragIcon()
{
	return static_cast<HCURSOR>(m_hIcon);
}

std::string WstringToString(const std::wstring str)
{// wstring转string
	unsigned len = str.size() * 4;
	setlocale(LC_CTYPE, "");
	char *p = new char[len];
	wcstombs(p, str.c_str(), len);
	std::string str1(p);
	delete[] p;
	return str1;
}

void CMatMFCDlg::OnBnClickedLoad()
{
	// TODO:  在此添加控件通知处理程序代码
	CFileDialog cfd(true, _T(".jpg"), NULL, OFN_FILEMUSTEXIST | OFN_HIDEREADONLY, _T("Image file   (*.jpg)|*.jpg|All   Files   (*.*)|*.*||"), this);
	if (cfd.DoModal() != IDOK)     // Tell if get the image  
	{
		return;
	}
	CString m_path = cfd.GetPathName();
	if (m_path == "")        //判断图片路径是否存在  
	{
		return;
	}
	std::wstring strpath;
	strpath = m_path.GetBuffer(0);

	input = cv::imread(WstringToString(strpath));
	DrawMat(input, IDC_IN1);

}

void CMatMFCDlg::OnBnClickedExit()
{
	// TODO:  在此添加控件通知处理程序代码
	int user_choice = MessageBox(L"您确定要退出吗？", L"退出", 1);
	if (user_choice == IDOK)
	{
		CDialog::OnCancel();
	}
}


void CMatMFCDlg::OnBnClickedSave()
{
	// TODO:  在此添加控件通知处理程序代码
	cv::Mat gray, mask, thr;
	cv::cvtColor(input, gray, cv::COLOR_BGR2GRAY);
	cv::threshold(gray, mask, 220, 255, cv::THRESH_BINARY_INV);
	cv::Mat mask_copy = mask;
	//cv::imshow("threshold", input);
	//cv::waitKey();

	cv::resize(mask, mask, cv::Size(mask.cols + 2, mask.rows + 2));
	floodFill(input, mask, cv::Point(10, 10), cv::Scalar(0, 0, 0), NULL, cv::Scalar(20, 20, 20), cv::Scalar(20, 20, 20));
	floodFill(input, mask, cv::Point(10, input.rows - 10), cv::Scalar(0, 0, 0), NULL, cv::Scalar(20, 20, 20), cv::Scalar(20, 20, 20));
	floodFill(input, mask, cv::Point(input.cols - 10, 10), cv::Scalar(0, 0, 0), NULL, cv::Scalar(20, 20, 20), cv::Scalar(20, 20, 20));
	floodFill(input, mask, cv::Point(input.cols - 10, input.rows - 10), cv::Scalar(0, 0, 0), NULL, cv::Scalar(20, 20, 20), cv::Scalar(20, 20, 20));
	//cv::imshow("flood", input);
	//cv::waitKey();

	cv::cvtColor(src, gray, cv::COLOR_BGR2GRAY);
	cv::threshold(gray, thr, 220, 255, cv::THRESH_BINARY_INV);

	int line = thr.rows - 1;
	bool stop = 0;
	for (int i = thr.rows - 1; i > -1; i--)
	{
		for (int j = 0; j < thr.cols; j++)
		{
			if (thr.at<uchar>(i, j) != 0)
			{
				line = i;
				stop = !stop;
				break;
			}
		}
		if (stop)
		{
			break;
		}
	}

	int step = 20;

	int height = src.rows - 2 * step - line;
	int width = height * thr.cols / thr.rows;

	cv::Rect rect = cv::Rect(src.cols/2 - width/2, src.rows - step - height, width, height);
	cv::GaussianBlur(input, input, cv::Size(3, 3), 1, 1);
	cv::resize(input, input, cv::Size(rect.width, rect.height));
	cv::resize(mask_copy, mask_copy, cv::Size(rect.width, rect.height));
	//cv::imshow("mask", mask);
	//cv::waitKey();
	input.copyTo(src(rect), mask_copy);
	DrawMat(src, IDC_OUT);
	cv::imwrite("src/output.jpg", src);
}
