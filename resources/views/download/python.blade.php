<!DOCTYPE html>
<html>
<head>
    <meta name="csrf-token" content="{{ csrf_token() }}">
    <link rel="stylesheet" href="{{ mix('css/app.css') }}">
    <title>Python</title>
</head>
<body>
    <div id="app">
        <header-component></header-component>
        <div class="content-wrapper">
            <div class="content">
                <div class="page-center-text">
                    <div>
                        <span class="page-title">PyTrampをプレイするにはPython実行環境が必要です。</span>
                    </div>
                </div>
                <h5><a href="javascript:;" onclick="Display('no1')">Windows</a></h5>
                <h5><a href="javascript:;" onclick="Display('no2')">Mac</a></h5>
                <div class="card">
                    <div class="card-body" id="SW1">
                      <h5 class="card-title">Python環境構築手順（Windows）</h5>
                      <p class="card-text"><span class="card-text-label">1. Pythonをインストール</span><br>Python公式サイト（https://www.python.org/）にアクセスし、「Download」からPythonをダウンロードします。</p>
                      <p class="card-text"><span class="card-text-label">2. PyTramp（本アプリ）をダウンロード</span><br><a href="/zip-download">こちらのボタン</a>からPyTrampをダウンロードできます。（Zip形式）</p>
                      <p class="card-text"><span class="card-text-label">3. Pythonを実行</span><br>分かりません分かりません。Pythonの実行方法が分かりません。</p>
                    </div>
                    <div class="card-body" id="SW2" style="display:none;">
                        <h5 class="card-title">Python環境構築手順（Mac）</h5>
                        <p class="card-text"><span class="card-text-label">1. Homebrewをインストール</span><br>ターミナルで下記を実行することでHomebrewをインストールします。<pre><code>/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"</code></pre></p>
                        <p class="card-text"><span class="card-text-label">2. pyenvをインストール</span><br>Homebrewを使ってpyenvをインストールします。<pre><code>brew install pyenv</code></pre></p>
                        <p class="card-text"><span class="card-text-label">3. pyenvの設定を行う</span><br>下記コマンドを順に実行することで、pyenvの設定を行います。<pre><code>echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile</code><code>echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile</code><code>echo 'eval "$(pyenv init -)"' >> ~/.bash_profile</code><code>source ~/.bash_profile</code></pre></p>
                        <p class="card-text"><span class="card-text-label">4. Pythonをインストール</span><br>pyenvを使ってPythonをインストールします。（今回はv3.6.5）<pre><code>pyenv install 3.6.5</code></pre></p>
                        <p class="card-text"><span class="card-text-label">5. PyTramp（本アプリ）をダウンロード</span><br><a href="/zip-download">こちらのボタン</a>からPyTrampをダウンロードできます。（Zip形式）</p>
                      <p class="card-text"><span class="card-text-label">6. Pythonを実行</span><br>分かりません分かりません。Pythonの実行方法が分かりません。</p>
                      </div>
                      <a href="/" class="btn btn-primary back">Topへ戻る</a>
                  </div>
            </div>
        </div>
    </div>
<script src=" {{ mix('js/app.js') }} "></script>
<script language="javascript" type="text/javascript">
function Display(no){
   if(no == "no1"){
       document.getElementById("SW1").style.display = "block";
       document.getElementById("SW2").style.display = "none";
   }else if(no == "no2"){
       document.getElementById("SW1").style.display = "none";
       document.getElementById("SW2").style.display = "block";
   }
}
</script>
</body>
</html>
