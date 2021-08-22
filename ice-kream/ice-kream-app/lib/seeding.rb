module IceKream
  class Seeding
    class << self

      def seed_admin(options={})
        AdminUser.create(
          email: options[:email] || "admin@example.com",
          password: options[:password] || "password123"
        )
      end

      def seed_cones(quantity=5)
        FactoryBot.create_list(:cone, quantity)
      end

      def seed_creams(quantity=5)
        FactoryBot.create_list(:cream, quantity)
      end

      def seed_combos(quantity)
        quantity.times do
          return unless seed_combo
        end
      end

      def find_free_pair_id_tuple
        existing_pairs = Combo.pluck(:cone_id, :cream_id)
        cone_ids = Cone.pluck(:id)
        cream_ids = Cream.pluck(:id)

        cone_ids.each do |cone_id|
          cream_ids.each do |cream_id|
            candidate_pair = [cone_id, cream_id]
            is_taken = existing_pairs.include? candidate_pair
            puts "candidate(#{candidate_pair}) in #{existing_pairs}: #{is_taken}"
            unless is_taken
              return candidate_pair
            end
          end
        end
        nil
      end

      def seed_combo
        if (pair = find_free_pair_id_tuple)
          cone_id, cream_id = pair
          Combo.create!(cone_id: cone_id, cream_id: cream_id)
          true
        end
        false
      end
    end
  end
end