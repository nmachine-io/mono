require 'octokit'

REPO_ID = "nmachine-io/consumer-frontend-desktop"
GH_SEC_NAME = "gh-token-delete-me-later"
DEB_NAME = "deb_release.deb"
WGET_PREFIX = "wget -q --auth-no-challenge --header='Accept:application/octet-stream'"
BUCKET_PREFIX = "gs://nmachine-public/releases"

RELEASE_TYPES = [
  { extension: ".deb", fname: DEB_NAME }
]

token = `gcloud secrets versions access latest --secret=#{GH_SEC_NAME}`
client = Octokit::Client.new(access_token: token)

releases = client.releases(REPO_ID, query: { type: 'created_at', sort: 'asc' })
latest_release = releases.first

if latest_release
  release_assets = latest_release[:assets] || []

  RELEASE_TYPES.each do |release_definition|
    extension, fname = release_definition.values_at(:extension, :fname)

    asset = release_assets.find { |a| a[:name].end_with?(extension) }
    authenticated_dl_url = asset[:url].gsub("//", "//#{token}:@")

    download_cmd = "#{WGET_PREFIX} #{authenticated_dl_url} -O #{fname}"
    puts "Downloading #{extension} into #{fname}..."
    system download_cmd

    puts "Uploading #{extension} to #{fname} #{BUCKET_PREFIX}/#{fname}..."
    upload_cmd = "gsutil cp #{fname} #{BUCKET_PREFIX}/#{fname}"
    system upload_cmd
  end
else
  puts "Repo has no latest release :/"
end