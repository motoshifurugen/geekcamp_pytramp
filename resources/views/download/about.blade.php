<!DOCTYPE html>
<html>
<head>
    <meta name="csrf-token" content="{{ csrf_token() }}">
    <link rel="stylesheet" href="{{ mix('css/app.css') }}">
    <title>About PyTramp</title>
</head>
<body>
    <div id="app">
        <header-component></header-component>
        <div class="content-wrapper">
            <div class="content">
                <div class="page-center-text">
                    <div>
                        <span class="page-title">このゲームのルール</span>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body">
                      <h5 class="card-title">数字の大小で勝負するシンプルなゲーム</h5>
                      <p class="card-text"><span class="card-text-label">■対戦人数</span><br>2人</p>
                      <p class="card-text"><span class="card-text-label">■ゲームの開始</span><br>各プレイヤーが1~Kまでのカードを1枚ずつ合計13枚の手札を持ってスタートします。</p>
                      <p class="card-text"><span class="card-text-label">■バトル</span><br>各プレイヤーが順番に1枚のカードを選びます。一度選んだカードは手札からなくなります。2人が選び終わるとそれぞれが選んだカードが表示されます。数字の大きかった方にWinがつきます。同じ数字の場合はDrawになります。</p>
                      <p class="card-text"><span class="card-text-label">■最終結果</span><br>合計13回のバトルを終えて、Winの回数が多かったプレイヤーの勝利となります。</p>
                      <p class="card-text"><span class="card-text-label">ゲームの面白さ</span><br>どの順番でカードを出すのか、相手に残っている手札はなんなのかを考えながらカードを選択するのが勝利への鍵となります。</p>
                      <a href="/" class="btn btn-primary back">Topへ戻る</a>
                    </div>
                  </div>
            </div>
        </div>
    </div>
<script src=" {{ mix('js/app.js') }} "></script>
</body>
</html>
