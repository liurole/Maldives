#include <opencv2/opencv.hpp>
// MatMFCDlg.h : ͷ�ļ�
//

#pragma once


// CMatMFCDlg �Ի���
class CMatMFCDlg : public CDialogEx
{
// ����
public:
	CMatMFCDlg(CWnd* pParent = NULL);	// ��׼���캯��

// �Ի�������
	enum { IDD = IDD_MATMFC_DIALOG };
	
	protected:
	virtual void DoDataExchange(CDataExchange* pDX);	// DDX/DDV ֧��

	cv::Mat src, input, output;
	void DrawMat(cv::Mat& img, UINT nID);

// ʵ��
protected:
	HICON m_hIcon;

	// ���ɵ���Ϣӳ�亯��
	virtual BOOL OnInitDialog();
	afx_msg void OnPaint();
	afx_msg HCURSOR OnQueryDragIcon();
	DECLARE_MESSAGE_MAP()
public:
	afx_msg void OnBnClickedLoad();
	afx_msg void OnBnClickedExit();
	afx_msg void OnBnClickedSave();
};
