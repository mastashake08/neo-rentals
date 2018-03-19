<?php

use Illuminate\Http\Request;
use App\Http\Resources\UserResource;
use App\Http\Resources\RentalsCollection;
use Illuminate\Support\Facades\Log;
/*
|--------------------------------------------------------------------------
| API Routes
|--------------------------------------------------------------------------
|
| Here is where you can register API routes for your application. These
| routes are loaded by the RouteServiceProvider within a group which
| is assigned the "api" middleware group. Enjoy building your API!
|
*/

Route::middleware('auth:api')->get('/me', function (Request $request) {
    return new UserResource($request->user());
});

Route::middleware('auth:api')->get('/rentals',function(Request $request){
  return new RentalsCollection(\App\Rental::all());
});
Route::post('publish',function(Request $request){
  Log::info($request->all());
  return response()->json([
    'code' => 0
  ]);
});
