import React, { Component } from 'react';
import { Link } from "react-router-dom";
import Row from 'react-bootstrap/Row';
import Col from 'react-bootstrap/Col';
import Container from 'react-bootstrap/Container'
import '../../styles/about.css'

class AboutMe extends Component {
	render() {
		return (
			<div>
				<Container>
					<Row>
						<Col style={divStyle}>
							<h1 style={{textAlign:"center"}}><b>Hello There!</b></h1>
						</Col>
					</Row>
					<hr />
					<Row>
						<Col md={6} style={divStyle}>
							<img title="Me at SGDQ 2018" height={250} width={250} src={"https://nigelhaney.me/imgs/sgdq_pic.jpg"} alt={""} />
						</Col>
						<Col md={6} className="textContainer" style={divStyle}>
							<p className="aboutText">I am Nigel, and thank you for visiting my website!
								I am excited to use this site as a platform to share my thoughts on various different subjects online. Read on to learn more about my background!</p>
						</Col>
					</Row>
					<Row>
						<Col>
							<hr />
						</Col>
					</Row>
					<Row>
						<Col md={6} className="textContainer" style={divStyle}>
							<p className="aboutText">I am a recent graduate (December, 2018) from Washington State University with
						   with a B.S in Computer Science. I am currently looking for my first job to start
						   my career in the tech industry. I am very passionate about technology and am always excited for new 
					   	opportunities to learn more. To see more information about my professional background, please check out my <Link to="/experience">experience page.</Link> Since I have no professional experience, I am trying out all different niches in the field to try to find my preferred <a rel="noopener noreferrer" target="_blank" href="https://youtu.be/3EuzHaKysKk?t=12">speciality</a>. Currently I am leaning towards a more backend-oriented role. 
							</p>
						</Col>
						<Col md={6} style={divStyle}>
							<img title="Go Cougs!" height={200} width={300} src={"https://nigelhaney.me/imgs/coug.svg"} alt={""} />
						</Col>
					</Row>
					<hr />
					<Row>
						<Col md={4} style={divStyle}>
							<img className="petPic" title="Moose on the grass" height={200} width={175} src={"https://nigelhaney.me/imgs/moose.jpg"} alt={"moose"} />
						</Col>
						<Col md={4}  style={divStyle}>
							<p className="aboutText">
								Outside of computer science, my hobbies are playing video games <a target="_blank" rel="noopener noreferrer" href="https://www.youtube.com/watch?v=T4j9RSNbssU"> quickly and competitively</a> and hanging out with my girlfriend and dogs Moose (the brown bear cub) and Luke (wearing the pumpkin hat). I hope to incorporate some of my other hobbies into my website in the form of blog posts in the future.
							</p>
						</Col>
						<Col md={4} style={divStyle}>
							<img className="petPic" title="Luke wearing his favorite hat" height={200} width={175} src={"https://nigelhaney.me/imgs/luke.jpg"} alt={"luke"} />
						</Col>
					</Row>
				</Container>
				<audio autoPlay ref="audio_tag" src={require("../../audio/obi-wan-hello-there.mp3")} />
			</div>
		);
	}
}

const divStyle = {
	textAlign:"center",
	//border: "1px solid black",
	alignItems: "center",
	justifyContet: "center"
}



export default AboutMe;