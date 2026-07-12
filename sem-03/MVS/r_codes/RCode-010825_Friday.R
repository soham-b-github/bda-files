install.packages("mvtnorm")
library(mvtnorm)

install.packages("plotly")
library(plotly)

mu = c(1,1)
Sigma = matrix(c(1,0.8,0.8,1), nrow=2)

# Create the Grid
x = seq(-5,5, length=50)
y = seq(-5,5, length=50)
grid = expand.grid(x=x,y=y)

# Calculate PDF values
z = matrix(dmvnorm(grid, mean=mu, sigma=Sigma), nrow=length(x), ncol=length(y))

# Interactive 3D surface plot with plotly
plot_ly(x=~x,y=~y,z=~z) %>%
  add_surface() %>%
  layout(title="Interactive 3D Surface Plot of Bivariate Normal PDF",
         scene = list(
           xaxis = list(title="x1"),
           yaxis = list(title="x2"),
           zaxis = list(title="Density")
         ))

