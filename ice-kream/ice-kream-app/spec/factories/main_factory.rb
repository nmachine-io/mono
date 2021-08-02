coating_options = %w[dough vanilla milk]
flavor_options = %w[apple orange pear]

def food_api_url(ingredient)
  "https://spoonacular.com/cdn/ingredients_100x100/#{ingredient}.jpg"
end

FactoryBot.define do
  factory :cone do
    name { Faker::Food.ingredient }
    image_url { food_api_url(coating_options.sample) }
  end

  factory :cream do
    name { Faker::Food.ingredient }
    image_url { food_api_url(flavor_options.sample) }
  end
end