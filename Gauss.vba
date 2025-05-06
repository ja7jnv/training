Sub Gauss()
'配列を宣言
Dim T(10) As Single, TN(10) As Single, TK(10) As Single, TIM As Single
'定数を指定
Const DT = 0.01, DX = 0.1
'変数rの計算
R = DT / DX / DX
 Cells(3, 16).Value = "r=" & R
'配列に値を代入
TIM = 0
'初期値
For i = 0 To 10
T(i) = 1
TN(i) = 1
TK(i) = 1
Next i
'境界条件
T(0) = 0
T(10) = 0
TN(0) = 0
TN(10) = 0
TK(0) = 0
TK(10) = 0
'反復計算の準備
For i = 0 To 10
TK(i) = T(i)
Next
'時間を進める
Do While j < 4
j = j + 1
'格子点iと番号の表示
Cells(2, 1).Value = "i"
Cells(2, 14).Value = "εmax"
For i = 0 To 10
Cells(2, i + 2).Value = i
Next i
'反復条件の設定
MAXEPS = 0.01
Do While MAXEPS > 0.001
k = k + 1
MAXEPS = 0
For i = 1 To 9
'Gauss-Seidelの反復法
T(i) = R / (1 + 2 * R) * (T(i - 1) + TK(i + 1)) + 1 / (1 + 2 * R) * TN(i)
EPS = Abs((T(i) - TK(i)) / T(i))
If EPS > MAXEPS Then
   MAXEPS = EPS
End If
 Cells(k + 2, 1).Value = "k=" & k
 Cells(k + 2, 2).Value = T(0)
 Cells(k + 2, i + 2).Value = T(i)
 Cells(k + 2, 12).Value = T(10)
 Cells(k + 2, 14).Value = MAXEPS
'If j <= 4 Then
'   Range("A1:O16").ClearContents
'End If
Next
'近似値の更新
For i = 0 To 10
TK(i) = T(i)
Next
Loop
k = 0
'時刻を記述、収束した近似値を現在時刻の値に置き換え
TIM = TIM + DT
   Cells(1, 1).Value = "t=" & TIM
   Cells(17 + j, 1).Value = "t=" & TIM
For i = 0 To 10
TN(i) = T(i)
TK(i) = T(i)
   Cells(17 + j, i + 2).Value = TN(i)
Next
   Cells(17 + j, i + 3).Value = MAXEPS
Loop
End Sub

