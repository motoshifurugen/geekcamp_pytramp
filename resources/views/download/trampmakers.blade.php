<!DOCTYPE html>
<html>
<head>
    <meta name="csrf-token" content="{{ csrf_token() }}">
    <link rel="stylesheet" href="{{ mix('css/app.css') }}">
    <title>TrampM4kers</title>
</head>
<body>
    <div id="app">
        <header-component></header-component>
        <div class="content-wrapper">
            <div class="content">
                <div class="page-center-text">
                    <div>
                        <span class="page-title">製作者紹介</span>
                    </div>
                </div>
                <div class="card">
                    <div class="card-body">
                      <h5 class="card-title">TrampM4kers「トランプメーカーズ」</h5>
                      <p class="card-text"><span class="card-text-label">ren_namimatsu
                    </span><br></p>
                      <p class="card-text"><span class="card-text-label">鈴木暖也</span><br></p>
                      <p class="card-text"><span class="card-text-label">M4SHR0</span><br></p>
                      <p class="card-text"><span class="card-text-label">motoshi_furugen</span><br></p>
                      <a href="/" class="btn btn-primary back">Topへ戻る</a>
                    </div>
                  </div>
            </div>
            </div>
        </div>
    </div>
<script src=" {{ mix('js/app.js') }} "></script>
</body>
</html>
