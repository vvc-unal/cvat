# Run

docker-compose -f docker-compose.vvc.yml -f components/cuda/docker-compose.cuda.yml up -d

# Stop

docker-compose -f docker-compose.vvc.yml -f components/cuda/docker-compose.cuda.yml down
