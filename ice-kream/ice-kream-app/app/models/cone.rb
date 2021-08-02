class Cone < ApplicationRecord
  has_many :combos, dependent: :destroy
end