<?php

use Illuminate\Support\Facades\Route;

/*
|--------------------------------------------------------------------------
| Web Routes
|--------------------------------------------------------------------------
|
| Here is where you can register web routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| contains the "web" middleware group. Now create something great!
|
*/

// Route::get('/', function () {
//     return view('welcome');
// });

Route::get('/', 'App\Http\Controllers\DownloadController@index');

Route::get('downloadFile', function () {
    return response()->download('../resources/img/sample.jpg');
});

Route::get('about', function () { return view('download/about'); });

Route::get('python', function () { return view('download/python'); });

Route::get('trampmakers', function () { return view('download/trampmakers'); });

Route::get('zip-download', function () {
    $files = glob(public_path().'/storage/files/*');
    $zip = new ZipArchive();
    $zip->open(public_path().'/pytramp.zip', ZipArchive::CREATE);
    foreach($files as $file){
        $file_info = pathinfo($file);
        $file_name = $file_info['filename'].'.'.$file_info['extension'];
        $zip->addFile($file, $file_name);
    }
    $zip->close();
    return response()->download(public_path().'/pytramp.zip');
});

