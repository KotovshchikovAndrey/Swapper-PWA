//@ts-ignore
import styles from "../index.module.css"
import React from "react"
import { Stack, Container, List, ListItem, Box, Typography } from "@mui/material"
import { OnScrollFadeInAnimation } from "utils/animations/fade"

export default function Manual() {
  React.useEffect(() => {
    const clearFunc = OnScrollFadeInAnimation(styles.manual_item)
    return clearFunc
  }, [])

  return (
    <React.Fragment>
      <Stack>
        <Typography className={styles.section_title} fontSize="25px" marginBottom="50px">
          Как пользоваться Swapper?
        </Typography>
        <Stack>
          <Container maxWidth="lg">
            <List
              sx={{
                display: "flex",
                flexDirection: "column",
                justifyContent: "center",
                alignItems: "center",
              }}
            >
              <ListItem
                className={styles.manual_item}
                sx={{
                  display: "flex",
                  flexDirection: "column",
                  maxWidth: 700,
                }}
              >
                <Typography
                  marginBottom="15px"
                  sx={{
                    fontSize: "20px",
                    alignSelf: "flex-start",
                  }}
                >
                  1. Вы обязаны рассказать друзьям
                </Typography>
                <Box src="http://localhost/images/doc.png" component="img" maxWidth="100%" />
              </ListItem>
              <ListItem
                className={styles.manual_item}
                sx={{
                  display: "flex",
                  flexDirection: "column",
                  maxWidth: 700,
                }}
              >
                <Typography
                  marginBottom="15px"
                  sx={{
                    fontSize: "20px",
                    alignSelf: "flex-start",
                  }}
                >
                  2. Вы должны этим пользоваться
                </Typography>
                <Box src="http://localhost/images/doc.png" component="img" maxWidth="100%" />
              </ListItem>
              <ListItem
                className={styles.manual_item}
                sx={{
                  display: "flex",
                  flexDirection: "column",
                  maxWidth: 700,
                }}
              >
                <Typography
                  marginBottom="15px"
                  sx={{
                    fontSize: "20px",
                    alignSelf: "flex-start",
                  }}
                >
                  3. Собственно пользуйтесь
                </Typography>
                <Box src="http://localhost/images/doc.png" component="img" maxWidth="100%" />
              </ListItem>
            </List>
          </Container>
        </Stack>
      </Stack>
    </React.Fragment>
  )
}
