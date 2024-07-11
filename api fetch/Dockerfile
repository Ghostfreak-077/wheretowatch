# FROM node:20-alpine

# # We use nodemon to restart the server every time there's a change

# WORKDIR /app

# COPY package.json .

# RUN npm install --production

# COPY . .

# EXPOSE 5001

# # Use script specified in package,json
# CMD ["npm", "run", "start"]
# # # CMD [ "ls", "-a" ]



# # Optimized
# # FROM node:20-alpine as builder
# # FROM node:20-alpine
# # WORKDIR /app
# # # COPY . .

# # EXPOSE 5000

# # # WORKDIR /app
# # COPY ./dist/index.js .
# # COPY ./data.json .
# # COPY .env .
# # CMD ["node", "index.js"]



FROM node:20-alpine
WORKDIR /app
COPY . .
RUN npm install --omit=dev && npm install -g @vercel/ncc && ncc build index.js -o dist && rm -rf node_modules
CMD ["node", "dist/index.js"]