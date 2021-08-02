class Cream < ApplicationRecord
  has_many :combos, dependent: :destroy
end