ActiveAdmin.register Cone do
  permit_params :name, :image_url, :coating

  # index do
  #   selectable_column
  #   id_column
  #   column :name
  #   # column 'Image' do |r|
  #   #   image_tag r.image_url, width: 60, height: 60
  #   # end
  #   column :coating
  #   actions
  # end
  #
  # filter :email
  # filter :current_sign_in_at
  # filter :sign_in_count
  # filter :created_at
  #
  # form do |f|
  #   f.inputs do
  #     f.input :email
  #     f.input :password
  #     f.input :password_confirmation
  #   end
  #   f.actions
  # end

end
