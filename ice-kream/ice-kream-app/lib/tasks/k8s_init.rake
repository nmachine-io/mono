namespace :db do
  task :init do
    max_tries = 10
    counter = 0
    until system("bundle exec rake db:version")
      puts "Db not found, attempting to create..."
      if system "bundle exec rake db:create"#, err: File::NULL
        puts "Db created successfully, migrating..."
        system "bundle exec rake db:migrate"
        # system "bundle exec rake db:seed"
      else
        counter += 1
        if counter < 10
          puts "Create failed ##{counter}/#{max_tries}, waiting 5 seconds"
          sleep 5.seconds
        else
          puts "Out of retries for create db:init, exit code 1"
          exit 1
        end
      end
    end
    puts "Db present, migrating..."
    system "bundle exec rake db:migrate"
    puts "db:init complete"
  end
end