//@ts-ignore
import styles from "../index.module.css"
import React from "react"
import { Stack, Container, List, ListItem, Box, Typography } from "@mui/material"
import { FadeInAnimation } from "../../../utils/animations/fade"

export default function Manual() {
	React.useEffect(() => {
		const clearFunc = FadeInAnimation(styles.manual_item)
		return clearFunc
	}, [])

	return (
		<React.Fragment>
			<Stack>
				<h2 className={styles.section_title}>Как пользоваться Swapper?</h2>
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
									sx={{ fontSize: "20px", alignSelf: "flex-start" }}
								>
									1. Вы обязаны рассказать друзьям
								</Typography>
								<Box
									component="img"
									src="http://localhost/images/doc.png"
									maxWidth="100%"
								/>
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
									sx={{ fontSize: "20px", alignSelf: "flex-start" }}
								>
									2. Вы должны этим пользоваться
								</Typography>
								<Box
									component="img"
									src="http://localhost/images/doc.png"
									maxWidth="100%"
								/>
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
									sx={{ fontSize: "20px", alignSelf: "flex-start" }}
								>
									3. Собственно пользуйтесь
								</Typography>
								<Box
									component="img"
									src="http://localhost/images/doc.png"
									maxWidth="100%"
								/>
							</ListItem>
						</List>
					</Container>
				</Stack>
			</Stack>
		</React.Fragment>
	)
}
