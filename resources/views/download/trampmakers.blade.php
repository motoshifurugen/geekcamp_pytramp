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
                <div class="center-text">
                    <div>
                        <span class="title">作成 TrampM4kers</span>
                    </div>
                    <div class="sub-title">
                        <span>Tramp Game Made In Python</span>
                    </div>
                    <div class="text-subtitle">2021.3.21 created by TrampM4kers</div>
                    <div class="downloadBox">
                        <a href="/downloadFile">PyTrampをダウンロードする</a>
                    </div>
                    <div class="button-box">
                        <a class="button-wrapper" href="{{ url('/about') }}">
                            <span class="button about"><span>PyTrampルール</span></span>
                        </a>
                        <a class="button-wrapper" href="{{ url('/python') }}">
                            <span class="button about"><span>Python実行環境構築</span></span>
                        </a>
                        <a class="button-wrapper" href="{{ url('/trampmakers') }}">
                            <span class="button about"><span>作成者紹介</span></span>
                        </a>
                    </div>
                </div>
            </div>
        </div>
    </div>
<script src=" {{ mix('js/app.js') }} "></script>
</body>
</html>
