<!DOCTYPE html>
<html>
<head>
    <meta name="csrf-token" content="{{ csrf_token() }}">
    <link rel="stylesheet" href="{{ mix('css/app.css') }}">
    <title>Top Page</title>
</head>
<body>
    <div id="app">
        <!-- デフォルトだとこの中ではvue.jsが有効 -->
        <!-- example-component はLaravelに入っているサンプルのコンポーネント -->
        {{-- <example-component></example-component> --}}
    </div>
    <div class="content">
        <div class="title">
            <p>{{ $appName }}</p>
        </div>
        <div class="downloadBox">
            <a href="/downloadFile">/downloadFile</a>
        </div>
    </div>
<script src=" {{ mix('js/app.js') }} "></script>
</body>
</html>
