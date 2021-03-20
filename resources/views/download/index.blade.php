<!DOCTYPE html>
<html>
<head>
    <title>Top Page</title>
    <style type="text/css">
    .content {
        text-align: center;
        background-color: coral;
        height: 680px;
        padding: 20px;
    }
    .title {
        font-family:'Franklin Gothic Medium', 'Arial Narrow', Arial, sans-serif;
        margin: 2em auto;
        font-size: 36px;
        border-bottom: solid 10px #FFFFFF;
        width: 50%;
    }
    .downloadBox {
        border: solid 1px black;
        background-color: cornflowerblue;
        width: 20%;
        margin: 2em auto;
        padding: 1em;
        border-radius: 1rem;
    }
    .downloadBox a{
        text-decoration: none;
        color: white;
        font-size: 16px;
    }
    </style>
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
