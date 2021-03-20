<!DOCTYPE html>
<html>
<head>
    <title>Top Page</title>
    <link rel="stylesheet" href="{{ asset('css/style.css') }}">
</head>
<body>
    <div class="content">
        <div class="title">
            <p>{{ $appName }}</p>
        </div>
        <div class="downloadBox">
            <a href="#" download="sample.jpg">サンプル画像を保存</a>
        </div>
    </div>
</body>
</html>
