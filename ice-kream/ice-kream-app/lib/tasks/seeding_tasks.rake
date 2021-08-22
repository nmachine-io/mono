require 'rake'

admin_args = %w[email password]
seed_deep_orgs_args = %w[cone_count cream_count combo_pct]

namespace :seed do

  task :admin, admin_args => :environment do |_, args|
    IceKream::Seeding.seed_admin(args.to_h)
  end

  task :products, seed_deep_orgs_args => :environment do |_, _args|
    args = _args.to_h

    cones = IceKream::Seeding.seed_cones(args[:cone_count].to_i)
    creams = IceKream::Seeding.seed_creams(args[:cream_count].to_i)

    combo_fraction = args[:combo_pct].to_f / 100
    combo_cones = cones.sample(cones.count * combo_fraction)
    combo_creams = creams.sample(creams.count * combo_fraction)

    combo_cones.each do |cone|
      combo_creams.each do |cream|
        Combo.create(cone: cone, cream: cream, name: Faker::Food.dish)
      end
    end
  end
end