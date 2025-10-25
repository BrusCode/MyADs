# Multi-stage build for React frontend

# ==============================================
# Base Stage - Common dependencies
# ==============================================
FROM node:22-alpine as base

# Set working directory
WORKDIR /app

# Copy package files
COPY package*.json ./

# ==============================================
# Development Stage
# ==============================================
FROM base as development

# Install all dependencies (including devDependencies)
RUN npm install

# Copy application code
COPY . .

# Expose port
EXPOSE 5173

# Start development server
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]

# ==============================================
# Build Stage
# ==============================================
FROM base as build

# Install dependencies
RUN npm ci --only=production

# Copy application code
COPY . .

# Build application
ARG VITE_API_URL
ENV VITE_API_URL=$VITE_API_URL

RUN npm run build

# ==============================================
# Production Stage
# ==============================================
FROM nginx:alpine as production

# Copy built files from build stage
COPY --from=build /app/dist /usr/share/nginx/html

# Copy nginx configuration
COPY nginx.conf /etc/nginx/conf.d/default.conf

# Expose port
EXPOSE 80

# Health check
HEALTHCHECK --interval=30s --timeout=10s --start-period=5s --retries=3 \
    CMD wget --no-verbose --tries=1 --spider http://localhost/ || exit 1

# Start nginx
CMD ["nginx", "-g", "daemon off;"]

