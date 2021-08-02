class AddEntities < ActiveRecord::Migration[5.2]
  def up
    create_table :cones do |t|
      t.string :name
      t.string :image_url
      t.timestamps null: true
    end

    create_table :creams do |t|
      t.string :name
      t.string :image_url
      t.timestamps null: true
    end

    create_table :combos do |t|
      t.string :name
      t.belongs_to :cone
      t.belongs_to :cream
      t.timestamps null: true
    end
  end

  def down
    drop_table :cones
    drop_table :creams
    drop_table :combos
  end

end
