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
                        <span class="python-page-title">PyTrampをプレイするためのPython環境構築</span>
                    </div>
                </div>
                <div class="button-box">
                    <a class="button-wrapper" href="javascript:;" onclick="Display('no1')">
                        <span class="button about"><span>Windows用</span></span>
                    </a>
                    <a class="button-wrapper" href="javascript:;" onclick="Display('no2')">
                        <span class="button about"><span>Mac用</span></span>
                    </a>
                </div>
                <div class="card">
                    <div class="card-body" id="SW1">
                      <h5 class="card-title">Python環境構築手順（Windows）</h5>
                      <p class="card-text"><span class="python-card-text-label">1. Pythonをインストール</span><br /><span class="python-card-text-span">Python公式サイト（https://www.python.org/）にアクセスし、「Download」からPythonをダウンロードします。</span></p><br />
                      <p class="card-text"><span class="python-card-text-label">2. PyTramp（本アプリ）をダウンロード</span><br /><span class="python-card-text-span"><span class="python-downloadBox"><a href="/zip-download">こちらのボタン</a></span>からPyTrampをダウンロードできます。（Zip形式）</span></p><br />
                      <p class="card-text"><span class="python-card-text-label">3. Pythonを実行</span><br /><span class="python-card-text-span">分かりません分かりません。Pythonの実行方法が分かりません。</span></p><br />
                    </div>
                    <div class="card-body" id="SW2" style="display:none;">
                        <h5 class="card-title">Python環境構築手順（Mac）</h5>
                        <p class="card-text"><span class="python-card-text-label">1. Homebrewをインストール</span><br /><span class="python-card-text-span">ターミナルで下記を実行することでHomebrewをインストールします。<pre><code>/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"</code></pre></span></p><br />
                        <p class="card-text"><span class="python-card-text-label">2. pyenvをインストール</span><br /><span class="python-card-text-span">Homebrewを使ってpyenvをインストールします。<pre><code>brew install pyenv</code></pre></span></p><br />
                        <p class="card-text"><span class="python-card-text-label">3. pyenvの設定を行う</span><br /><span class="python-card-text-span">下記コマンドを順に実行することで、pyenvの設定を行います。<pre><code>echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile</code><code>echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile</code><code>echo 'eval "$(pyenv init -)"' >> ~/.bash_profile</code><code>source ~/.bash_profile</code></pre></span></p><br />
                        <p class="card-text"><span class="python-card-text-label">4. Pythonをインストール</span><br /><span class="python-card-text-span">pyenvを使ってPythonをインストールします。（今回はv3.6.5）<pre><code>pyenv install 3.6.5</code></pre></span></p><br />
                        <p class="card-text"><span class="python-card-text-label">5. PyTramp（本アプリ）をダウンロード</span><br /><span class="python-card-text-span"><span class="python-downloadBox"><a href="/zip-download">こちらのボタン</a></span>からPyTrampをダウンロードできます。（Zip形式）</span></p><br />
                      <p class="card-text"><span class="python-card-text-label">6. Pythonを実行</span><br /><span class="python-card-text-span">分かりません分かりません。Pythonの実行方法が分かりません。</span></p><br />
                      </div>
                      <a href="/" class="btn btn-primary python-back">Topへ戻る</a>
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
