<?php

use Faker\Generator as Faker;

/*
|--------------------------------------------------------------------------
| Model Factories
|--------------------------------------------------------------------------
|
| This directory should contain each of the model factory definitions for
| your application. Factories provide a convenient way to generate new
| model instances for testing / seeding your application's database.
|
*/

$factory->define(App\Rental::class, function (Faker $faker) {
    return [
        'user_id' => 1,
        'address' => $faker->streetAddress,
        'city' => $faker->city, // secret
        'state' => $faker->state,
        'zip' => $faker->postcode,
        'photo' => $faker->imageUrl($width = 640, $height = 480),
        'description' => $faker->paragraph,
        'down_deposit' => $faker->randomFloat($nbMaxDecimals = 8, $min = 3, $max = 10),
        'monthly_rent' => $faker->randomFloat($nbMaxDecimals = 8, $min = 3, $max = 10),
        'is_rented' => false
    ];
});
