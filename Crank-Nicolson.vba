Rem Attribute VBA_ModuleType=VBAModule
Option VBASupport 1

Sub jacobi()
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
Next

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
Do While j < 5
    j = j + 1
    TIM = TIM + DT
    
    '格子点iと番号の表示
    Cells(16, 1).Value = "i"
    
    For i = 0 To 10
        Cells(16, i + 2).Value = i
    Next
    
    Cells(16, 14).Value = "εmax"
    
    '反復条件の設定
    MAXEPS = 0.01
    Do While MAXEPS > 0.001
        k = k + 1
        MAXEPS = 0
        
        For i = 1 To 9
            'Jacobiの反復法
            'T(i) = R / (1 + 2 * R) * (TK(i - 1) + TK(i + 1)) + 1 / (1 + 2 * R) * TN(i)
            
            'クランク・ニコルソン法
            T(i) = R / 2 / (1 + R) * (TK(i - 1) + TK(i + 1)) + 1 / 2 / (1 + R) * (R * TN(i - 1) + 2 * (1 - R) * TN(i) + R * TN(i + 1))
            
            EPS = Abs((T(i) - TK(i)) / T(i))

            If EPS > MAXEPS Then
                MAXEPS = EPS
            End If
            
            Worksheets(2).Cells(L + k + 1, 1).Value = "k=" & k
            Worksheets(2).Cells(L + k + 1, 2).Value = T(0)
            Worksheets(2).Cells(L + k + 1, i + 2).Value = T(i)
            Worksheets(2).Cells(L + k + 1, 12).Value = T(10)
            Worksheets(2).Cells(L + k + 1, 14).Value = MAXEPS
            Worksheets(2).Cells(L + k + 2, 1).Value = "t=" & TIM
        Next

        '近似値の計算
        For i = 0 To 10
            TK(i) = T(i)
        Next
    Loop

    L = L + k + 3
    k = 0
    
    '時刻を記述、収束した近似値を現在時刻に置き換え
    Cells(17 + j, 1).Value = "t=" & TIM
    
    For i = 0 To 10
        TN(i) = T(i)
        TK(i) = T(i)
        Cells(17 + j, i + 2).Value = TN(i)
    Next
    
    Cells(17 + j, i + 3).Value = MAXEPS

Loop

End Sub
