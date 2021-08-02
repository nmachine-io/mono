class Constants
  class << self
    def app_name
      'ice-kream'
    end

    def key_base_secret_name
      'backend-secret-key-base'
    end

    def db_creds_secret_name
      "db-creds"
    end

    def postgres_name
      'postgres'
    end

    def pvc_name
      "postgres-pvc"
    end

    def backend_name
      'monolith'
    end

    def backend_secret_name
      "#{self.app_name}-secret"
    end
  end
end