<?php

namespace App\Http\Controllers;

use Illuminate\Http\Request;

class DownloadController extends Controller
{
    public function index()
    {
        $appName = 'PyTrampダウンロードアプリ';
        return view('download/index', compact('appName'));
    }
}
